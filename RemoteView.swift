import SwiftUI

struct RemoteView: View {
    @EnvironmentObject var sessionManager: SessionManager
    let onDisconnect: () -> Void
    
    @State private var isConnected = false
    @State private var sessionTime = 0
    @State private var showDisconnectConfirm = false
    @State private var timer: Timer?
    
    var body: some View {
        ZStack {
            // Main remote desktop area
            VStack(spacing: 0) {
                // Top control bar
                HStack {
                    // Left: Status
                    HStack(spacing: 16) {
                        // Connection status
                        HStack(spacing: 8) {
                            Circle()
                                .fill(isConnected ? Color.green : Color.yellow)
                                .frame(width: 10, height: 10)
                                .overlay(
                                    Circle()
                                        .stroke(isConnected ? Color.green : Color.yellow, lineWidth: 2)
                                        .scaleEffect(1.5)
                                        .opacity(0)
                                        .animation(.easeInOut(duration: 1.0).repeatForever(autoreverses: false), value: isConnected)
                                )
                            Text(sessionManager.currentMachine?.uppercased() ?? "UNKNOWN")
                                .font(.system(size: 18, weight: .bold))
                                .foregroundColor(.white)
                        }
                        
                        Divider()
                            .frame(height: 24)
                        
                        // Session info
                        Text("Session: \(sessionManager.currentSessionId?.suffix(8) ?? "N/A")")
                            .font(.system(size: 12))
                            .foregroundColor(.white.opacity(0.6))
                        
                        Text("Duration: \(formatTime(sessionTime))")
                            .font(.system(size: 12))
                            .foregroundColor(.white.opacity(0.6))
                    }
                    
                    Spacer()
                    
                    // Right: Controls
                    HStack(spacing: 12) {
                        ControlButton(icon: "camera.fill", label: "Screenshot")
                        ControlButton(icon: "mic.fill", label: "Audio")
                        ControlButton(icon: "folder.fill", label: "Files")
                        
                        Divider()
                            .frame(height: 24)
                        
                        Button(action: { showDisconnectConfirm = true }) {
                            HStack(spacing: 6) {
                                Image(systemName: "xmark.circle.fill")
                                Text("Disconnect")
                                    .font(.system(size: 13, weight: .semibold))
                            }
                            .foregroundColor(.white)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                            .background(
                                RoundedRectangle(cornerRadius: 8)
                                    .fill(Color.red.opacity(0.8))
                            )
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                }
                .padding(.horizontal, 24)
                .padding(.vertical, 16)
                .background(
                    Color.black.opacity(0.9)
                        .overlay(
                            Divider()
                                .background(Color.white.opacity(0.1)),
                            alignment: .bottom
                        )
                )
                
                // Remote desktop canvas
                ZStack {
                    Color.black
                    
                    if !isConnected {
                        // Connecting state
                        VStack(spacing: 24) {
                            ProgressView()
                                .progressViewStyle(CircularProgressViewStyle(tint: Color(hex: "ff3366")))
                                .scaleEffect(2.0)
                            
                            Text("Establishing secure connection...")
                                .font(.system(size: 24))
                                .foregroundColor(.white)
                            
                            Text("Connecting to \(sessionManager.currentMachine?.uppercased() ?? "UNKNOWN")")
                                .font(.system(size: 14))
                                .foregroundColor(.white.opacity(0.6))
                        }
                    } else {
                        // Connected state - Demo screen
                        VStack(spacing: 32) {
                            Text("🖥️")
                                .font(.system(size: 96))
                            
                            Text("Connected to \(sessionManager.currentMachine?.uppercased() ?? "UNKNOWN")")
                                .font(.system(size: 36, weight: .bold))
                                .foregroundColor(.white)
                            
                            Text("Screen sharing active")
                                .font(.system(size: 24))
                                .foregroundColor(Color(hex: "00ff88"))
                            
                            VStack(alignment: .leading, spacing: 16) {
                                IntegrationRow(title: "macOS Screen Sharing", detail: "Enable in System Preferences → Sharing → Screen Sharing")
                                IntegrationRow(title: "VNC Server", detail: "Built-in macOS VNC server (port 5900)")
                                IntegrationRow(title: "noVNC", detail: "HTML5 VNC client for web browsers")
                                IntegrationRow(title: "RustDesk", detail: "Open-source TeamViewer alternative")
                            }
                            .padding(32)
                            .background(
                                RoundedRectangle(cornerRadius: 16)
                                    .fill(Color.white.opacity(0.05))
                                    .overlay(
                                        RoundedRectangle(cornerRadius: 16)
                                            .stroke(Color(hex: "ff3366").opacity(0.3), lineWidth: 1)
                                    )
                            )
                        }
                        .padding(40)
                    }
                }
                
                // Bottom status bar
                HStack {
                    HStack(spacing: 24) {
                        StatusBadge(icon: "lock.fill", text: "Encrypted Connection")
                        StatusBadge(icon: "doc.text.fill", text: "Session Logged")
                        StatusBadge(icon: "video.fill", text: "Recording Active")
                    }
                    
                    Spacer()
                    
                    Text("Fish Music Inc - CB_01 • NOIZYLAB v1.0")
                        .font(.system(size: 10))
                        .foregroundColor(.white.opacity(0.3))
                }
                .padding(.horizontal, 24)
                .padding(.vertical, 12)
                .background(
                    Color.black.opacity(0.9)
                        .overlay(
                            Divider()
                                .background(Color.white.opacity(0.1)),
                            alignment: .top
                        )
                )
            }
            
            // Disconnect confirmation dialog
            if showDisconnectConfirm {
                Color.black.opacity(0.7)
                    .ignoresSafeArea()
                    .onTapGesture {
                        showDisconnectConfirm = false
                    }
                
                VStack(spacing: 24) {
                    Text("End Session?")
                        .font(.system(size: 32, weight: .bold))
                        .foregroundColor(.white)
                    
                    Text("Are you sure you want to disconnect from \(sessionManager.currentMachine?.uppercased() ?? "UNKNOWN")?")
                        .font(.system(size: 16))
                        .foregroundColor(.white.opacity(0.8))
                        .multilineTextAlignment(.center)
                    
                    Text("Session duration: \(formatTime(sessionTime))")
                        .font(.system(size: 14))
                        .foregroundColor(.white.opacity(0.5))
                    
                    HStack(spacing: 16) {
                        Button(action: { showDisconnectConfirm = false }) {
                            Text("Cancel")
                                .font(.system(size: 16, weight: .semibold))
                                .foregroundColor(.white)
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 14)
                                .background(
                                    RoundedRectangle(cornerRadius: 12)
                                        .fill(Color.white.opacity(0.1))
                                )
                        }
                        .buttonStyle(PlainButtonStyle())
                        
                        Button(action: {
                            timer?.invalidate()
                            onDisconnect()
                        }) {
                            Text("Disconnect")
                                .font(.system(size: 16, weight: .semibold))
                                .foregroundColor(.white)
                                .frame(maxWidth: .infinity)
                                .padding(.vertical, 14)
                                .background(
                                    RoundedRectangle(cornerRadius: 12)
                                        .fill(Color.red)
                                )
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                }
                .padding(40)
                .frame(width: 500)
                .background(
                    RoundedRectangle(cornerRadius: 20)
                        .fill(Color(hex: "1a1a2e"))
                        .overlay(
                            RoundedRectangle(cornerRadius: 20)
                                .stroke(Color.white.opacity(0.1), lineWidth: 1)
                        )
                )
                .shadow(radius: 40)
            }
        }
        .onAppear {
            // Simulate connection
            DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
                withAnimation {
                    isConnected = true
                }
            }
            
            // Start timer
            timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
                sessionTime += 1
            }
        }
        .onDisappear {
            timer?.invalidate()
        }
    }
    
    private func formatTime(_ seconds: Int) -> String {
        let h = seconds / 3600
        let m = (seconds % 3600) / 60
        let s = seconds % 60
        return String(format: "%02d:%02d:%02d", h, m, s)
    }
}

struct ControlButton: View {
    let icon: String
    let label: String
    @State private var isHovered = false
    
    var body: some View {
        Button(action: {}) {
            HStack(spacing: 6) {
                Image(systemName: icon)
                Text(label)
                    .font(.system(size: 13))
            }
            .foregroundColor(.white.opacity(0.8))
            .padding(.horizontal, 12)
            .padding(.vertical, 8)
            .background(
                RoundedRectangle(cornerRadius: 8)
                    .fill(Color.white.opacity(isHovered ? 0.15 : 0.05))
            )
        }
        .buttonStyle(PlainButtonStyle())
        .onHover { hovering in
            isHovered = hovering
        }
    }
}

struct StatusBadge: View {
    let icon: String
    let text: String
    
    var body: some View {
        HStack(spacing: 6) {
            Image(systemName: icon)
                .font(.system(size: 10))
            Text(text)
                .font(.system(size: 11))
        }
        .foregroundColor(.white.opacity(0.5))
    }
}

struct IntegrationRow: View {
    let title: String
    let detail: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 4) {
            Text(title)
                .font(.system(size: 14, weight: .semibold))
                .foregroundColor(Color(hex: "ff3366"))
            Text(detail)
                .font(.system(size: 12))
                .foregroundColor(.white.opacity(0.6))
        }
    }
}
