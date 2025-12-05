import Foundation
import Combine

class SessionManager: ObservableObject {
    @Published var currentMachine: String?
    @Published var currentSessionId: String?
    @Published var isActive: Bool = false
    
    private var sessions: [RemoteSession] = []
    
    func startSession(machine: String, sessionId: String) {
        currentMachine = machine
        currentSessionId = sessionId
        isActive = true
        
        let session = RemoteSession(
            id: sessionId,
            machine: machine,
            startTime: Date(),
            endTime: nil
        )
        sessions.append(session)
        
        logEvent("Session started: \(machine) (\(sessionId))")
    }
    
    func endSession() {
        if let sessionId = currentSessionId,
           let index = sessions.firstIndex(where: { $0.id == sessionId }) {
            sessions[index].endTime = Date()
            logEvent("Session ended: \(currentMachine ?? "unknown") (\(sessionId))")
        }
        
        currentMachine = nil
        currentSessionId = nil
        isActive = false
    }
    
    private func logEvent(_ message: String) {
        let timestamp = ISO8601DateFormatter().string(from: Date())
        print("[\(timestamp)] NOIZYLAB: \(message)")
        
        // Write to log file
        let logPath = FileManager.default.homeDirectoryForCurrentUser
            .appendingPathComponent("Library/Logs/NoizyLabRemote")
        
        try? FileManager.default.createDirectory(at: logPath, withIntermediateDirectories: true)
        
        let logFile = logPath.appendingPathComponent("sessions.log")
        let logEntry = "[\(timestamp)] \(message)\n"
        
        if let data = logEntry.data(using: .utf8) {
            if FileManager.default.fileExists(atPath: logFile.path) {
                if let fileHandle = try? FileHandle(forWritingTo: logFile) {
                    fileHandle.seekToEndOfFile()
                    fileHandle.write(data)
                    fileHandle.closeFile()
                }
            } else {
                try? data.write(to: logFile)
            }
        }
    }
}

struct RemoteSession: Identifiable {
    let id: String
    let machine: String
    let startTime: Date
    var endTime: Date?
}
