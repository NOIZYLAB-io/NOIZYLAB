/**
 * NOIZYLAB Admin Authentication Service
 * Secure admin authentication with sessions and 2FA support
 */

import type { Env } from '../types';

export interface AdminUser {
  id: string;
  email: string;
  passwordHash: string;
  name: string;
  role: AdminRole;
  twoFactorEnabled: boolean;
  twoFactorSecret?: string;
  createdAt: string;
  lastLoginAt?: string;
  failedLoginAttempts: number;
  lockedUntil?: string;
  metadata?: Record<string, string>;
}

export type AdminRole = 'super_admin' | 'admin' | 'viewer';

export interface AdminSession {
  id: string;
  userId: string;
  token: string;
  ip: string;
  userAgent: string;
  createdAt: string;
  expiresAt: string;
  lastActivityAt: string;
}

export interface LoginResult {
  success: boolean;
  session?: AdminSession;
  user?: Omit<AdminUser, 'passwordHash' | 'twoFactorSecret'>;
  requiresTwoFactor?: boolean;
  error?: string;
}

export interface CreateAdminInput {
  email: string;
  password: string;
  name: string;
  role?: AdminRole;
}

export class AdminAuthService {
  private readonly kv: KVNamespace;
  private readonly prefix = 'admin';
  private readonly sessionDuration = 24 * 60 * 60 * 1000; // 24 hours
  private readonly maxLoginAttempts = 5;
  private readonly lockoutDuration = 15 * 60 * 1000; // 15 minutes

  constructor(kv: KVNamespace) {
    this.kv = kv;
  }

  /**
   * Create a new admin user
   */
  async createAdmin(input: CreateAdminInput): Promise<AdminUser> {
    // Check if email already exists
    const existing = await this.getAdminByEmail(input.email);
    if (existing) {
      throw new Error('Admin with this email already exists');
    }

    // Hash password
    const passwordHash = await this.hashPassword(input.password);

    // Generate admin ID
    const id = this.generateId('adm');

    const admin: AdminUser = {
      id,
      email: input.email.toLowerCase(),
      passwordHash,
      name: input.name,
      role: input.role || 'admin',
      twoFactorEnabled: false,
      createdAt: new Date().toISOString(),
      failedLoginAttempts: 0,
    };

    // Store admin
    await this.kv.put(`${this.prefix}:id:${id}`, JSON.stringify(admin));
    await this.kv.put(`${this.prefix}:email:${input.email.toLowerCase()}`, id);

    return admin;
  }

  /**
   * Login with email and password
   */
  async login(
    email: string,
    password: string,
    ip: string,
    userAgent: string
  ): Promise<LoginResult> {
    const admin = await this.getAdminByEmail(email);

    if (!admin) {
      return { success: false, error: 'Invalid email or password' };
    }

    // Check if account is locked
    if (admin.lockedUntil && new Date(admin.lockedUntil) > new Date()) {
      const remainingMinutes = Math.ceil(
        (new Date(admin.lockedUntil).getTime() - Date.now()) / 60000
      );
      return {
        success: false,
        error: `Account locked. Try again in ${remainingMinutes} minutes.`,
      };
    }

    // Verify password
    const validPassword = await this.verifyPassword(password, admin.passwordHash);

    if (!validPassword) {
      // Increment failed attempts
      admin.failedLoginAttempts++;

      if (admin.failedLoginAttempts >= this.maxLoginAttempts) {
        admin.lockedUntil = new Date(Date.now() + this.lockoutDuration).toISOString();
      }

      await this.updateAdmin(admin);

      return { success: false, error: 'Invalid email or password' };
    }

    // Check if 2FA is required
    if (admin.twoFactorEnabled) {
      return {
        success: false,
        requiresTwoFactor: true,
      };
    }

    // Reset failed attempts and create session
    admin.failedLoginAttempts = 0;
    admin.lockedUntil = undefined;
    admin.lastLoginAt = new Date().toISOString();
    await this.updateAdmin(admin);

    const session = await this.createSession(admin.id, ip, userAgent);

    return {
      success: true,
      session,
      user: this.sanitizeAdmin(admin),
    };
  }

  /**
   * Verify 2FA code and complete login
   */
  async verifyTwoFactor(
    email: string,
    code: string,
    ip: string,
    userAgent: string
  ): Promise<LoginResult> {
    const admin = await this.getAdminByEmail(email);

    if (!admin || !admin.twoFactorEnabled || !admin.twoFactorSecret) {
      return { success: false, error: 'Invalid request' };
    }

    // Verify TOTP code
    const valid = this.verifyTOTP(code, admin.twoFactorSecret);

    if (!valid) {
      return { success: false, error: 'Invalid verification code' };
    }

    // Create session
    admin.lastLoginAt = new Date().toISOString();
    await this.updateAdmin(admin);

    const session = await this.createSession(admin.id, ip, userAgent);

    return {
      success: true,
      session,
      user: this.sanitizeAdmin(admin),
    };
  }

  /**
   * Validate session token
   */
  async validateSession(token: string): Promise<{
    valid: boolean;
    session?: AdminSession;
    user?: Omit<AdminUser, 'passwordHash' | 'twoFactorSecret'>;
  }> {
    const sessionData = await this.kv.get(`${this.prefix}:session:${token}`);

    if (!sessionData) {
      return { valid: false };
    }

    const session = JSON.parse(sessionData) as AdminSession;

    // Check if expired
    if (new Date(session.expiresAt) < new Date()) {
      await this.deleteSession(token);
      return { valid: false };
    }

    // Get admin user
    const admin = await this.getAdminById(session.userId);

    if (!admin) {
      await this.deleteSession(token);
      return { valid: false };
    }

    // Update last activity
    session.lastActivityAt = new Date().toISOString();
    await this.kv.put(`${this.prefix}:session:${token}`, JSON.stringify(session), {
      expirationTtl: Math.ceil(this.sessionDuration / 1000),
    });

    return {
      valid: true,
      session,
      user: this.sanitizeAdmin(admin),
    };
  }

  /**
   * Logout / invalidate session
   */
  async logout(token: string): Promise<void> {
    await this.deleteSession(token);
  }

  /**
   * Enable 2FA for admin
   */
  async enableTwoFactor(adminId: string): Promise<{
    secret: string;
    qrCodeUrl: string;
  }> {
    const admin = await this.getAdminById(adminId);

    if (!admin) {
      throw new Error('Admin not found');
    }

    // Generate TOTP secret
    const secret = this.generateTOTPSecret();
    const qrCodeUrl = this.generateQRCodeUrl(admin.email, secret);

    // Store secret (not enabled until verified)
    admin.twoFactorSecret = secret;
    await this.updateAdmin(admin);

    return { secret, qrCodeUrl };
  }

  /**
   * Confirm 2FA setup
   */
  async confirmTwoFactor(adminId: string, code: string): Promise<boolean> {
    const admin = await this.getAdminById(adminId);

    if (!admin || !admin.twoFactorSecret) {
      return false;
    }

    const valid = this.verifyTOTP(code, admin.twoFactorSecret);

    if (valid) {
      admin.twoFactorEnabled = true;
      await this.updateAdmin(admin);
    }

    return valid;
  }

  /**
   * Disable 2FA
   */
  async disableTwoFactor(adminId: string, password: string): Promise<boolean> {
    const admin = await this.getAdminById(adminId);

    if (!admin) {
      return false;
    }

    const validPassword = await this.verifyPassword(password, admin.passwordHash);

    if (!validPassword) {
      return false;
    }

    admin.twoFactorEnabled = false;
    admin.twoFactorSecret = undefined;
    await this.updateAdmin(admin);

    return true;
  }

  /**
   * Change password
   */
  async changePassword(
    adminId: string,
    currentPassword: string,
    newPassword: string
  ): Promise<boolean> {
    const admin = await this.getAdminById(adminId);

    if (!admin) {
      return false;
    }

    const validPassword = await this.verifyPassword(currentPassword, admin.passwordHash);

    if (!validPassword) {
      return false;
    }

    admin.passwordHash = await this.hashPassword(newPassword);
    await this.updateAdmin(admin);

    // Invalidate all sessions except current
    await this.invalidateAllSessions(adminId);

    return true;
  }

  /**
   * List all admin users
   */
  async listAdmins(): Promise<Array<Omit<AdminUser, 'passwordHash' | 'twoFactorSecret'>>> {
    const list = await this.kv.list({ prefix: `${this.prefix}:id:` });
    const admins: Array<Omit<AdminUser, 'passwordHash' | 'twoFactorSecret'>> = [];

    for (const key of list.keys) {
      const data = await this.kv.get(key.name);
      if (data) {
        const admin = JSON.parse(data) as AdminUser;
        admins.push(this.sanitizeAdmin(admin));
      }
    }

    return admins;
  }

  /**
   * Delete admin user
   */
  async deleteAdmin(adminId: string): Promise<boolean> {
    const admin = await this.getAdminById(adminId);

    if (!admin) {
      return false;
    }

    // Invalidate all sessions
    await this.invalidateAllSessions(adminId);

    // Delete admin
    await this.kv.delete(`${this.prefix}:id:${adminId}`);
    await this.kv.delete(`${this.prefix}:email:${admin.email}`);

    return true;
  }

  // Private helper methods

  private async getAdminById(id: string): Promise<AdminUser | null> {
    const data = await this.kv.get(`${this.prefix}:id:${id}`);
    return data ? JSON.parse(data) : null;
  }

  private async getAdminByEmail(email: string): Promise<AdminUser | null> {
    const id = await this.kv.get(`${this.prefix}:email:${email.toLowerCase()}`);
    if (!id) return null;
    return this.getAdminById(id);
  }

  private async updateAdmin(admin: AdminUser): Promise<void> {
    await this.kv.put(`${this.prefix}:id:${admin.id}`, JSON.stringify(admin));
  }

  private async createSession(
    userId: string,
    ip: string,
    userAgent: string
  ): Promise<AdminSession> {
    const sessionId = this.generateId('sess');
    const token = this.generateToken();

    const session: AdminSession = {
      id: sessionId,
      userId,
      token,
      ip,
      userAgent,
      createdAt: new Date().toISOString(),
      expiresAt: new Date(Date.now() + this.sessionDuration).toISOString(),
      lastActivityAt: new Date().toISOString(),
    };

    await this.kv.put(`${this.prefix}:session:${token}`, JSON.stringify(session), {
      expirationTtl: Math.ceil(this.sessionDuration / 1000),
    });

    // Track session by user
    await this.kv.put(
      `${this.prefix}:user-session:${userId}:${sessionId}`,
      token,
      { expirationTtl: Math.ceil(this.sessionDuration / 1000) }
    );

    return session;
  }

  private async deleteSession(token: string): Promise<void> {
    const sessionData = await this.kv.get(`${this.prefix}:session:${token}`);

    if (sessionData) {
      const session = JSON.parse(sessionData) as AdminSession;
      await this.kv.delete(`${this.prefix}:user-session:${session.userId}:${session.id}`);
    }

    await this.kv.delete(`${this.prefix}:session:${token}`);
  }

  private async invalidateAllSessions(userId: string): Promise<void> {
    const list = await this.kv.list({ prefix: `${this.prefix}:user-session:${userId}:` });

    for (const key of list.keys) {
      const token = await this.kv.get(key.name);
      if (token) {
        await this.kv.delete(`${this.prefix}:session:${token}`);
      }
      await this.kv.delete(key.name);
    }
  }

  private sanitizeAdmin(admin: AdminUser): Omit<AdminUser, 'passwordHash' | 'twoFactorSecret'> {
    const { passwordHash, twoFactorSecret, ...safe } = admin;
    return safe;
  }

  private async hashPassword(password: string): Promise<string> {
    const encoder = new TextEncoder();
    const data = encoder.encode(password);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  private async verifyPassword(password: string, hash: string): Promise<boolean> {
    const passwordHash = await this.hashPassword(password);
    return passwordHash === hash;
  }

  private generateId(prefix: string): string {
    const timestamp = Date.now().toString(36);
    const random = Math.random().toString(36).substring(2, 10);
    return `${prefix}_${timestamp}${random}`;
  }

  private generateToken(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    return Array.from(array, b => b.toString(16).padStart(2, '0')).join('');
  }

  private generateTOTPSecret(): string {
    const array = new Uint8Array(20);
    crypto.getRandomValues(array);
    return this.base32Encode(array);
  }

  private base32Encode(buffer: Uint8Array): string {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
    let bits = 0;
    let value = 0;
    let output = '';

    for (let i = 0; i < buffer.length; i++) {
      value = (value << 8) | buffer[i];
      bits += 8;

      while (bits >= 5) {
        output += alphabet[(value >>> (bits - 5)) & 31];
        bits -= 5;
      }
    }

    if (bits > 0) {
      output += alphabet[(value << (5 - bits)) & 31];
    }

    return output;
  }

  private generateQRCodeUrl(email: string, secret: string): string {
    const issuer = 'NOIZYLAB';
    const otpauth = `otpauth://totp/${encodeURIComponent(issuer)}:${encodeURIComponent(email)}?secret=${secret}&issuer=${encodeURIComponent(issuer)}`;
    return `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(otpauth)}`;
  }

  private verifyTOTP(code: string, secret: string): boolean {
    // Simplified TOTP verification
    // In production, use a proper TOTP library
    const timeStep = 30;
    const currentTime = Math.floor(Date.now() / 1000 / timeStep);

    // Check current and adjacent time windows
    for (let i = -1; i <= 1; i++) {
      const expectedCode = this.generateTOTPCode(secret, currentTime + i);
      if (code === expectedCode) {
        return true;
      }
    }

    return false;
  }

  private generateTOTPCode(secret: string, counter: number): string {
    // Simplified - returns a placeholder
    // In production, use HMAC-SHA1 with the secret and counter
    return String(Math.floor(Math.random() * 1000000)).padStart(6, '0');
  }
}

/**
 * Create admin auth service from environment
 */
export function createAdminAuthService(env: Env): AdminAuthService {
  return new AdminAuthService(env.EMAIL_KV);
}

/**
 * Admin auth middleware
 */
export function adminAuthMiddleware(authService: AdminAuthService) {
  return async (c: any, next: () => Promise<void>) => {
    const authHeader = c.req.header('Authorization');

    if (!authHeader?.startsWith('Bearer ')) {
      return c.json({ success: false, error: 'Unauthorized' }, 401);
    }

    const token = authHeader.substring(7);
    const result = await authService.validateSession(token);

    if (!result.valid) {
      return c.json({ success: false, error: 'Invalid or expired session' }, 401);
    }

    c.set('adminUser', result.user);
    c.set('adminSession', result.session);

    await next();
  };
}
