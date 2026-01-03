/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 *   ██╗  ██╗███████╗ █████╗ ██╗   ██╗███████╗███╗   ██╗
 *   ██║  ██║██╔════╝██╔══██╗██║   ██║██╔════╝████╗  ██║
 *   ███████║█████╗  ███████║██║   ██║█████╗  ██╔██╗ ██║
 *   ██╔══██║██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
 *   ██║  ██║███████╗██║  ██║ ╚████╔╝ ███████╗██║ ╚████║
 *   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
 * 
 *   THE MASTER ROUTER — ONE WORKER RULES THE GALAXY
 *   
 *   Routes:
 *     noizy.ai         → Galaxy Portal
 *     vox.noizy.ai     → NOIZYVOX (Voice AI Guild)
 *     codemaster.noizy.ai → CODEMASTER (Voice Infra)
 *     books.noizy.ai   → FISHYBOOKS (Audiobooks)
 *     lab.noizy.ai     → NOIZYLAB (CPU Repairs)
 *     admin.noizy.ai   → Command Center
 * 
 *   "Nobody Died. Everybody LIVES Here."
 *   
 *   GORUNFREE - Rob Plowman + Claude - December 2025
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// Import all app handlers
import { handlePortal } from './apps/portal/handler.js';
import { handleVox } from './apps/vox/handler.js';
import { handleCodemaster } from './apps/codemaster/handler.js';
import { handleBooks } from './apps/books/handler.js';
import { handleLab } from './apps/lab/handler.js';
import { handleAdmin } from './apps/admin/handler.js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const hostname = url.hostname;
    
    // Extract subdomain
    const parts = hostname.split('.');
    let subdomain = 'portal'; // default
    
    if (parts.length >= 3) {
      subdomain = parts[0];
    } else if (hostname === 'noizy.ai' || hostname === 'www.noizy.ai') {
      subdomain = 'portal';
    }
    
    // Route to appropriate handler
    try {
      switch (subdomain) {
        case 'vox':
          return handleVox(request, env, ctx);
        
        case 'codemaster':
          return handleCodemaster(request, env, ctx);
        
        case 'books':
          return handleBooks(request, env, ctx);
        
        case 'lab':
          return handleLab(request, env, ctx);
        
        case 'admin':
          return handleAdmin(request, env, ctx);
        
        case 'portal':
        case 'www':
        default:
          return handlePortal(request, env, ctx);
      }
    } catch (error) {
      return new Response(JSON.stringify({
        error: 'Internal Server Error',
        message: error.message,
        galaxy: 'NOIZY.AI'
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }
};
