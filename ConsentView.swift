import SwiftUI

struct ConsentView: View {
    @EnvironmentObject var sessionManager: SessionManager
    let onConsent: (Bool) -> Void
    
    @State private var scale: CGFloat = 0.8
    @State private var opacity: Double = 0
    
    var body: some View {
        VStack {
            Spacer()
            
            // Consent Envelope
            VStack(spacing: 30) {
                // Header
                VStack(spacing: 16) {
                    Text("🌌")
                        .font(.system(size: 72))
                    
                    HStack(spacing: 12) {
                        Text("CONSENT")
                            .foregroundColor(Color(hex: "ff3366"))
                        Text("RITUAL")
                            .foregroundColor(.white)
                    }
                    .font(.system(size: 48, weight: .black, design: .rounded))
                    
                    Text("Remote Access Request")
                        .font(.system(size: 20))
                        .foregroundColor(.white.opacity(0.6))
                }
                
                // Details
                VStack(spacing: 16) {
                    // Machine info
                    HStack(spacing: 40) {
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Target Machine")
                                .font(.system(size: 12))
                                .foregroundColor(.white.opacity(0.5))
                            Text(sessionManager.currentMachine?.uppercased() ?? "UNKNOWN")
                                .font(.system(size: 24, weight: .bold))
                                .foregroundColor(Color(hex: "ff3366"))
                        }
                        
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Session ID")
                                .font(.system(size: 12))
                                .foregroundColor(.white.opacity(0.5))
                            Text(sessionManager.currentSessionId?.suffix(8) ?? "N/A")
                                .font(.system(size: 14, design: .monospaced))
                                .foregroundColor(.white.opacity(0.7))
                        }
                    }
                    .padding(24)
                    .frame(maxWidth: .infinity)
                    .background(
                        RoundedRectangle(cornerRadius: 16)
                            .fill(Color.white.opacity(0.05))
                    )
                    
                    // Permissions
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Permissions Requested")
                            .font(.system(size: 12))
                            .foregroundColor(.white.opacity(0.5))
                        
                        PermissionRow(icon: "✓", text: "Screen viewing (read-only)", granted: true)
                        PermissionRow(icon: "✓", text: "Keyboard & mouse control", granted: true)
                        PermissionRow(icon: "✓", text: "Session recording (audit trail)", granted: true)
                    }
                    .padding(24)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(
                        RoundedRectangle(cornerRadius: 16)
                            .fill(Color.white.opacity(0.05))
                    )
                    
                    // Warning
                    HStack(spacing: 12) {
                        Text("⚠️")
                            .font(.system(size: 20))
                        VStack(alignment: .leading, spacing: 4) {
                            Text("User Agency Notice")
                                .font(.system(size: 12, weight: .bold))
                                .foregroundColor(Color.yellow)
                            Text("This remote session will be fully logged. You can disconnect at any time. All actions are subject to audit.")
                                .font(.system(size: 11))
                                .foregroundColor(Color.yellow.opacity(0.8))
                        }
                    }
                    .padding(16)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color.yellow.opacity(0.1))
                            .overlay(
                                RoundedRectangle(cornerRadius: 12)
                                    .stroke(Color.yellow.opacity(0.3), lineWidth: 1)
                            )
                    )
                }
                
                // Question
                VStack(spacing: 12) {
                    Text("Do you consent to this remote access session?")
                        .font(.system(size: 24, weight: .semibold))
                        .foregroundColor(.white)
                        .multilineTextAlignment(.center)
                    
                    Text("Requested by: Client Portal • \(Date().formatted(date: .abbreviated, time: .shortened))")
                        .font(.system(size: 12))
                        .foregroundColor(.white.opacity(0.4))
                }
                .padding(.vertical, 8)
                
                // Buttons
                HStack(spacing: 16) {
                    ConsentButton(
                        text: "✓ GRANT CONSENT",
                        color: Color.green,
                        action: { onConsent(true) }
                    )
                    
                    ConsentButton(
                        text: "✗ DENY",
                        color: Color.red,
                        action: { onConsent(false) }
                    )
                }
                
                // Footer
                VStack(spacing: 4) {
                    Text("Ritual ID: \(sessionManager.currentSessionId ?? "N/A")")
                    Text("Fish Music Inc - CB_01 • NOIZYLAB v1.0")
                }
                .font(.system(size: 10))
                .foregroundColor(.white.opacity(0.3))
                .padding(.top, 16)
            }
            .padding(40)
            .frame(width: 700)
            .background(
                RoundedRectangle(cornerRadius: 24)
                    .fill(Color.white.opacity(0.05))
                    .overlay(
                        RoundedRectangle(cornerRadius: 24)
                            .stroke(
                                LinearGradient(
                                    colors: [Color(hex: "ff3366"), Color(hex: "ffaa00")],
                                    startPoint: .topLeading,
                                    endPoint: .bottomTrailing
                                ),
                                lineWidth: 3
                            )
                    )
            )
            .shadow(color: Color(hex: "ff3366").opacity(0.3), radius: 30)
            .scaleEffect(scale)
            .opacity(opacity)
            
            Spacer()
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .onAppear {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.7)) {
                scale = 1.0
                opacity = 1.0
            }
        }
    }
}

struct PermissionRow: View {
    let icon: String
    let text: String
    let granted: Bool
    
    var body: some View {
        HStack(spacing: 12) {
            Text(icon)
                .font(.system(size: 14))
                .foregroundColor(granted ? .green : .gray)
            Text(text)
                .font(.system(size: 14))
                .foregroundColor(.white.opacity(0.8))
        }
    }
}

struct ConsentButton: View {
    let text: String
    let color: Color
    let action: () -> Void
    
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            Text(text)
                .font(.system(size: 16, weight: .bold))
                .foregroundColor(.white)
                .frame(maxWidth: .infinity)
                .padding(.vertical, 16)
                .background(
                    RoundedRectangle(cornerRadius: 12)
                        .fill(color.opacity(isHovered ? 1.0 : 0.8))
                )
                .scaleEffect(isHovered ? 1.05 : 1.0)
                .animation(.spring(response: 0.3), value: isHovered)
        }
        .buttonStyle(PlainButtonStyle())
        .onHover { hovering in
            isHovered = hovering
        }
    }
}
