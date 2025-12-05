import SwiftUI
import ScreenCaptureKit

/// 🔥 ADVANCED REMOTE VIEW - WITH ALL THE FUCKING FEATURES!
@available(macOS 13.0, *)
struct AdvancedRemoteView: View {
    @EnvironmentObject var sessionManager: SessionManager
    @StateObject private var screenCapture = ScreenCaptureManager()
    @StateObject private var networkManager = NetworkManager()
    @StateObject private var fileTransfer = FileTransferManager()
    @StateObject private var chat = ChatManager()
    @StateObject private var recording = RecordingManager()
    @StateObject private var multiDisplay = MultiDisplayManager()
    
    @State private var showChat = false
    @State private var showFileTransfer = false
    @State private var showDisplayPicker = false
    @State private var showShortcuts = false
    @State private var sessionTime = 0
    @State private var isFullscreen = false
    
    let onDisconnect: () -> Void
    
    private let shortcuts = KeyboardShortcutsManager()
    private let timer = Timer.publish(every: 1, on: .main, in: .common).autoconnect()
    
    var body: some View {
        ZStack {
            // Main remote desktop canvas
            if let capturedImage = screenCapture.capturedImage {
                Image(decorative: capturedImage, scale: 1.0)
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
            } else {
                // Loading / Connecting
                VStack(spacing: 24) {
                    ProgressView()
                        .scaleEffect(2.0)
                    Text("Establishing connection...")
                        .font(.title)
                }
            }
            
            // Overlay UI (if not fullscreen)
            if !isFullscreen {
                VStack(spacing: 0) {
                    // Top bar
                    TopControlBar(
                        machineName: sessionManager.currentMachine ?? "Unknown",
                        sessionID: sessionManager.currentSessionId ?? "",
                        sessionTime: sessionTime,
                        isRecording: recording.isRecording,
                        recordingDuration: recording.recordingDuration,
                        fps: screenCapture.fps,
                        onScreenshot: takeScreenshot,
                        onToggleRecording: toggleRecording,
                        onToggleChat: { showChat.toggle() },
                        onToggleFiles: { showFileTransfer.toggle() },
                        onDisconnect: onDisconnect
                    )
                    
                    Spacer()
                    
                    // Bottom status bar
                    BottomStatusBar(
                        connectedClients: networkManager.connectedClients,
                        networkStatus: networkManager.isConnected,
                        displayInfo: getCurrentDisplayInfo()
                    )
                }
            }
            
            // Chat overlay
            if showChat {
                ChatOverlay(chat: chat, onClose: { showChat = false })
            }
            
            // File transfer overlay
            if showFileTransfer {
                FileTransferOverlay(fileTransfer: fileTransfer, onClose: { showFileTransfer = false })
            }
            
            // Display picker
            if showDisplayPicker {
                DisplayPickerOverlay(
                    displays: multiDisplay.displays,
                    selectedID: multiDisplay.selectedDisplayID,
                    onSelect: { id in
                        multiDisplay.selectDisplay(id)
                        Task {
                            try? await screenCapture.stopCapture()
                            try? await screenCapture.startCapture(for: id)
                        }
                        showDisplayPicker = false
                    },
                    onClose: { showDisplayPicker = false }
                )
            }
            
            // Keyboard shortcuts help
            if showShortcuts {
                ShortcutsHelpOverlay(onClose: { showShortcuts = false })
            }
        }
        .onAppear {
            setupSession()
        }
        .onDisappear {
            teardownSession()
        }
        .onReceive(timer) { _ in
            sessionTime += 1
        }
    }
    
    private func setupSession() {
        // Start screen capture
        Task {
            await multiDisplay.discoverDisplays()
            try? await screenCapture.startCapture(for: multiDisplay.selectedDisplayID)
        }
        
        // Start network server
        try? networkManager.startServer()
        
        // Setup keyboard shortcuts
        shortcuts.onScreenshot = takeScreenshot
        shortcuts.onToggleChat = { showChat.toggle() }
        shortcuts.onToggleFullscreen = { isFullscreen.toggle() }
        shortcuts.onToggleRecording = toggleRecording
        shortcuts.onDisconnect = onDisconnect
        shortcuts.startMonitoring()
    }
    
    private func teardownSession() {
        Task {
            try? await screenCapture.stopCapture()
            if recording.isRecording {
                await recording.stopRecording()
            }
        }
        networkManager.stopServer()
        shortcuts.stopMonitoring()
    }
    
    private func takeScreenshot() {
        guard let image = screenCapture.capturedImage else { return }
        
        // Save to desktop
        let desktop = FileManager.default.urls(for: .desktopDirectory, in: .userDomainMask)[0]
        let filename = "Screenshot_\(Date().timeIntervalSince1970).png"
        let url = desktop.appendingPathComponent(filename)
        
        if let dest = CGImageDestinationCreateWithURL(url as CFURL, kUTTypePNG, 1, nil) {
            CGImageDestinationAddImage(dest, image, nil)
            CGImageDestinationFinalize(dest)
            print("📸 Screenshot saved: \(url.path)")
        }
    }
    
    private func toggleRecording() {
        Task {
            if recording.isRecording {
                await recording.stopRecording()
            } else {
                if let image = screenCapture.capturedImage {
                    try? recording.startRecording(
                        sessionID: sessionManager.currentSessionId ?? "unknown",
                        size: CGSize(width: image.width, height: image.height)
                    )
                }
            }
        }
    }
    
    private func getCurrentDisplayInfo() -> String {
        if let displayID = multiDisplay.selectedDisplayID,
           let display = multiDisplay.displays.first(where: { $0.id == displayID }) {
            return "\(display.name) • \(display.resolution)"
        }
        return "No display selected"
    }
}

// MARK: - Top Control Bar
struct TopControlBar: View {
    let machineName: String
    let sessionID: String
    let sessionTime: Int
    let isRecording: Bool
    let recordingDuration: TimeInterval
    let fps: Int
    let onScreenshot: () -> Void
    let onToggleRecording: () -> Void
    let onToggleChat: () -> Void
    let onToggleFiles: () -> Void
    let onDisconnect: () -> Void
    
    var body: some View {
        HStack {
            // Left: Status
            HStack(spacing: 12) {
                Circle()
                    .fill(Color.green)
                    .frame(width: 10, height: 10)
                Text(machineName.uppercased())
                    .font(.system(size: 16, weight: .bold))
                
                Text("•")
                    .foregroundColor(.white.opacity(0.3))
                
                Text(formatTime(sessionTime))
                    .font(.system(size: 12, design: .monospaced))
                
                if isRecording {
                    HStack(spacing: 4) {
                        Circle()
                            .fill(Color.red)
                            .frame(width: 8, height: 8)
                        Text("REC \(formatTime(Int(recordingDuration)))")
                            .font(.system(size: 12, weight: .bold))
                            .foregroundColor(.red)
                    }
                }
                
                Text("\(fps) FPS")
                    .font(.system(size: 12))
                    .foregroundColor(.white.opacity(0.5))
            }
            
            Spacer()
            
            // Right: Controls
            HStack(spacing: 8) {
                IconButton(icon: "camera.fill", action: onScreenshot)
                IconButton(icon: isRecording ? "record.circle.fill" : "record.circle", action: onToggleRecording)
                IconButton(icon: "message.fill", action: onToggleChat)
                IconButton(icon: "folder.fill", action: onToggleFiles)
                
                Divider()
                    .frame(height: 20)
                
                Button(action: onDisconnect) {
                    HStack(spacing: 6) {
                        Image(systemName: "xmark.circle.fill")
                        Text("Disconnect")
                    }
                    .font(.system(size: 13, weight: .semibold))
                    .foregroundColor(.white)
                    .padding(.horizontal, 12)
                    .padding(.vertical, 6)
                    .background(Color.red.opacity(0.8))
                    .cornerRadius(8)
                }
                .buttonStyle(PlainButtonStyle())
            }
        }
        .padding(.horizontal, 20)
        .padding(.vertical, 12)
        .background(Color.black.opacity(0.9))
    }
    
    private func formatTime(_ seconds: Int) -> String {
        let h = seconds / 3600
        let m = (seconds % 3600) / 60
        let s = seconds % 60
        return String(format: "%02d:%02d:%02d", h, m, s)
    }
}

// MARK: - Bottom Status Bar
struct BottomStatusBar: View {
    let connectedClients: [String]
    let networkStatus: Bool
    let displayInfo: String
    
    var body: some View {
        HStack {
            HStack(spacing: 16) {
                Label("Encrypted", systemImage: "lock.fill")
                Label("Logged", systemImage: "doc.text.fill")
                if networkStatus {
                    Label("\(connectedClients.count) Clients", systemImage: "network")
                }
                Label(displayInfo, systemImage: "display")
            }
            .font(.system(size: 11))
            .foregroundColor(.white.opacity(0.5))
            
            Spacer()
            
            Text("NOIZYLAB Remote v1.0 • Fish Music Inc")
                .font(.system(size: 10))
                .foregroundColor(.white.opacity(0.3))
        }
        .padding(.horizontal, 20)
        .padding(.vertical, 8)
        .background(Color.black.opacity(0.9))
    }
}

// MARK: - Icon Button
struct IconButton: View {
    let icon: String
    let action: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            Image(systemName: icon)
                .font(.system(size: 16))
                .foregroundColor(.white.opacity(0.8))
                .frame(width: 32, height: 32)
                .background(Color.white.opacity(isHovered ? 0.15 : 0.05))
                .cornerRadius(6)
        }
        .buttonStyle(PlainButtonStyle())
        .onHover { isHovered = $0 }
    }
}

// MARK: - Chat Overlay
struct ChatOverlay: View {
    @ObservedObject var chat: ChatManager
    let onClose: () -> Void
    
    @State private var messageText = ""
    
    var body: some View {
        HStack {
            Spacer()
            
            VStack(spacing: 0) {
                // Header
                HStack {
                    Text("💬 Chat")
                        .font(.headline)
                    Spacer()
                    Button(action: onClose) {
                        Image(systemName: "xmark.circle.fill")
                            .font(.title3)
                    }
                    .buttonStyle(PlainButtonStyle())
                }
                .padding()
                .background(Color(hex: "1a1a2e"))
                
                // Messages
                ScrollView {
                    VStack(spacing: 12) {
                        ForEach(chat.messages) { message in
                            ChatMessageBubble(message: message)
                        }
                    }
                    .padding()
                }
                
                // Input
                HStack {
                    TextField("Type a message...", text: $messageText)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Button("Send") {
                        if !messageText.isEmpty {
                            chat.sendMessage(messageText, to: "remote")
                            messageText = ""
                        }
                    }
                    .buttonStyle(.borderedProminent)
                }
                .padding()
                .background(Color(hex: "1a1a2e"))
            }
            .frame(width: 350)
            .background(Color.black.opacity(0.95))
            .cornerRadius(12)
            .shadow(radius: 20)
        }
        .padding()
    }
}

// MARK: - Chat Message Bubble
struct ChatMessageBubble: View {
    let message: ChatMessage
    
    var body: some View {
        HStack {
            if message.isSentByMe { Spacer() }
            
            VStack(alignment: message.isSentByMe ? .trailing : .leading, spacing: 4) {
                Text(message.text)
                    .padding(.horizontal, 12)
                    .padding(.vertical, 8)
                    .background(message.isSentByMe ? Color(hex: "ff3366") : Color.white.opacity(0.1))
                    .cornerRadius(12)
                
                Text(message.formattedTime)
                    .font(.caption2)
                    .foregroundColor(.white.opacity(0.4))
            }
            
            if !message.isSentByMe { Spacer() }
        }
    }
}

// MARK: - File Transfer Overlay
struct FileTransferOverlay: View {
    @ObservedObject var fileTransfer: FileTransferManager
    let onClose: () -> Void
    
    var body: some View {
        HStack {
            Spacer()
            
            VStack(spacing: 0) {
                // Header
                HStack {
                    Text("📁 File Transfer")
                        .font(.headline)
                    Spacer()
                    Button("Clear") {
                        fileTransfer.clearCompleted()
                    }
                    Button(action: onClose) {
                        Image(systemName: "xmark.circle.fill")
                            .font(.title3)
                    }
                    .buttonStyle(PlainButtonStyle())
                }
                .padding()
                .background(Color(hex: "1a1a2e"))
                
                // Transfers list
                ScrollView {
                    VStack(spacing: 8) {
                        ForEach(fileTransfer.transfers) { transfer in
                            FileTransferRow(transfer: transfer)
                        }
                    }
                    .padding()
                }
                
                // Drop zone
                Text("Drag files here to send")
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(Color.white.opacity(0.05))
                    .cornerRadius(8)
                    .padding()
            }
            .frame(width: 400)
            .background(Color.black.opacity(0.95))
            .cornerRadius(12)
            .shadow(radius: 20)
        }
        .padding()
    }
}

// MARK: - File Transfer Row
struct FileTransferRow: View {
    let transfer: FileTransfer
    
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Image(systemName: "doc.fill")
                Text(transfer.fileName)
                    .font(.system(size: 14))
                Spacer()
                Text(transfer.formattedSize)
                    .font(.caption)
                    .foregroundColor(.white.opacity(0.5))
            }
            
            ProgressView(value: transfer.progress)
                .progressViewStyle(.linear)
            
            Text(statusText)
                .font(.caption)
                .foregroundColor(statusColor)
        }
        .padding()
        .background(Color.white.opacity(0.05))
        .cornerRadius(8)
    }
    
    private var statusText: String {
        switch transfer.status {
        case .preparing: return "Preparing..."
        case .transferring: return "Sending... \(Int(transfer.progress * 100))%"
        case .receiving: return "Receiving... \(Int(transfer.progress * 100))%"
        case .completed: return "✓ Completed"
        case .cancelled: return "✗ Cancelled"
        case .failed: return "✗ Failed"
        }
    }
    
    private var statusColor: Color {
        switch transfer.status {
        case .completed: return .green
        case .cancelled, .failed: return .red
        default: return .white.opacity(0.6)
        }
    }
}

// MARK: - Display Picker Overlay
struct DisplayPickerOverlay: View {
    let displays: [DisplayInfo]
    let selectedID: String?
    let onSelect: (String) -> Void
    let onClose: () -> Void
    
    var body: some View {
        ZStack {
            Color.black.opacity(0.7)
                .ignoresSafeArea()
                .onTapGesture { onClose() }
            
            VStack(spacing: 20) {
                Text("Select Display")
                    .font(.title)
                
                ForEach(displays) { display in
                    Button(action: { onSelect(display.id) }) {
                        HStack {
                            VStack(alignment: .leading, spacing: 4) {
                                Text(display.name)
                                    .font(.headline)
                                Text(display.resolution)
                                    .font(.caption)
                                    .foregroundColor(.white.opacity(0.6))
                            }
                            
                            Spacer()
                            
                            if display.isPrimary {
                                Text("Primary")
                                    .font(.caption)
                                    .padding(.horizontal, 8)
                                    .padding(.vertical, 4)
                                    .background(Color(hex: "ff3366"))
                                    .cornerRadius(4)
                            }
                            
                            if display.id == selectedID {
                                Image(systemName: "checkmark.circle.fill")
                                    .foregroundColor(.green)
                            }
                        }
                        .padding()
                        .background(Color.white.opacity(0.1))
                        .cornerRadius(12)
                    }
                    .buttonStyle(PlainButtonStyle())
                }
            }
            .padding(40)
            .background(Color(hex: "1a1a2e"))
            .cornerRadius(20)
        }
    }
}

// MARK: - Shortcuts Help Overlay
struct ShortcutsHelpOverlay: View {
    let onClose: () -> Void
    
    var body: some View {
        ZStack {
            Color.black.opacity(0.7)
                .ignoresSafeArea()
                .onTapGesture { onClose() }
            
            VStack(spacing: 20) {
                Text("⌨️ Keyboard Shortcuts")
                    .font(.title)
                
                VStack(spacing: 12) {
                    ForEach(KeyboardShortcut.allShortcuts, id: \.keys) { shortcut in
                        HStack {
                            Text(shortcut.keys)
                                .font(.system(size: 16, design: .monospaced))
                                .foregroundColor(Color(hex: "ff3366"))
                            Spacer()
                            Text(shortcut.description)
                        }
                        .padding(.horizontal)
                    }
                }
                
                Button("Close") {
                    onClose()
                }
                .buttonStyle(.borderedProminent)
            }
            .padding(40)
            .background(Color(hex: "1a1a2e"))
            .cornerRadius(20)
        }
    }
}
