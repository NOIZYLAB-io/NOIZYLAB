import Foundation
import Network

/// 🌐 NETWORK STREAMING - SEND SCREEN OVER NETWORK
class NetworkManager: ObservableObject {
    @Published var isConnected = false
    @Published var connectedClients: [String] = []
    
    private var listener: NWListener?
    private var connections: [NWConnection] = []
    
    // MARK: - Start Server
    func startServer(port: UInt16 = 8888) throws {
        let params = NWParameters.tcp
        params.allowLocalEndpointReuse = true
        
        listener = try NWListener(using: params, on: NWEndpoint.Port(integerLiteral: port))
        
        listener?.stateUpdateHandler = { [weak self] state in
            switch state {
            case .ready:
                print("✅ Server ready on port \(port)")
                Task { @MainActor in
                    self?.isConnected = true
                }
            case .failed(let error):
                print("❌ Server failed: \(error)")
            default:
                break
            }
        }
        
        listener?.newConnectionHandler = { [weak self] connection in
            self?.handleNewConnection(connection)
        }
        
        listener?.start(queue: .global(qos: .userInitiated))
    }
    
    // MARK: - Handle New Connection
    private func handleNewConnection(_ connection: NWConnection) {
        connection.stateUpdateHandler = { [weak self] state in
            switch state {
            case .ready:
                print("✅ Client connected: \(connection.endpoint)")
                self?.connections.append(connection)
                Task { @MainActor in
                    if case .hostPort(let host, _) = connection.endpoint {
                        self?.connectedClients.append(host.debugDescription)
                    }
                }
            case .failed(let error):
                print("❌ Connection failed: \(error)")
            case .cancelled:
                print("📡 Connection cancelled")
                self?.removeConnection(connection)
            default:
                break
            }
        }
        
        connection.start(queue: .global(qos: .userInitiated))
        
        // Start receiving messages
        receiveMessage(from: connection)
    }
    
    // MARK: - Send Frame
    func sendFrame(_ imageData: Data, to connection: NWConnection) {
        // Frame format: [4 bytes: size][N bytes: image data]
        var sizeData = Data()
        var size = UInt32(imageData.count).bigEndian
        sizeData.append(Data(bytes: &size, count: 4))
        
        let frameData = sizeData + imageData
        
        connection.send(content: frameData, completion: .contentProcessed { error in
            if let error = error {
                print("❌ Send error: \(error)")
            }
        })
    }
    
    // MARK: - Broadcast Frame
    func broadcastFrame(_ imageData: Data) {
        for connection in connections {
            sendFrame(imageData, to: connection)
        }
    }
    
    // MARK: - Receive Message
    private func receiveMessage(from connection: NWConnection) {
        connection.receive(minimumIncompleteLength: 1, maximumLength: 65536) { [weak self] data, _, isComplete, error in
            if let data = data, !data.isEmpty {
                // Handle incoming data (mouse/keyboard events)
                self?.handleRemoteInput(data)
            }
            
            if isComplete {
                self?.removeConnection(connection)
            } else if error == nil {
                // Continue receiving
                self?.receiveMessage(from: connection)
            }
        }
    }
    
    // MARK: - Handle Remote Input
    private func handleRemoteInput(_ data: Data) {
        // Parse remote input commands
        // Format: [1 byte: type][N bytes: data]
        guard let type = data.first else { return }
        
        switch type {
        case 0x01: // Mouse move
            if data.count >= 9 {
                let x = data[1..<5].withUnsafeBytes { $0.load(as: Float.self) }
                let y = data[5..<9].withUnsafeBytes { $0.load(as: Float.self) }
                // Handle mouse move
                print("🖱️ Mouse: (\(x), \(y))")
            }
        case 0x02: // Mouse click
            print("🖱️ Click")
        case 0x03: // Keyboard
            if let char = String(data: data.dropFirst(), encoding: .utf8) {
                print("⌨️ Key: \(char)")
            }
        default:
            break
        }
    }
    
    // MARK: - Stop Server
    func stopServer() {
        listener?.cancel()
        connections.forEach { $0.cancel() }
        connections.removeAll()
        
        Task { @MainActor in
            isConnected = false
            connectedClients.removeAll()
        }
    }
    
    // MARK: - Remove Connection
    private func removeConnection(_ connection: NWConnection) {
        connections.removeAll { $0 === connection }
        Task { @MainActor in
            if case .hostPort(let host, _) = connection.endpoint {
                connectedClients.removeAll { $0 == host.debugDescription }
            }
        }
    }
}
