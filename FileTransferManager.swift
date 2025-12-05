import Foundation
import AppKit

/// 📁 FILE TRANSFER - DRAG & DROP FILES BETWEEN MACHINES
class FileTransferManager: ObservableObject {
    @Published var transfers: [FileTransfer] = []
    @Published var totalProgress: Double = 0
    
    // MARK: - Send File
    func sendFile(_ url: URL, to destination: String) async throws {
        let transfer = FileTransfer(
            id: UUID(),
            fileName: url.lastPathComponent,
            fileSize: try FileManager.default.attributesOfItem(atPath: url.path)[.size] as? Int64 ?? 0,
            progress: 0,
            status: .preparing
        )
        
        await MainActor.run {
            transfers.append(transfer)
        }
        
        // Read file data
        let data = try Data(contentsOf: url)
        
        // Send in chunks (1MB each)
        let chunkSize = 1024 * 1024
        var offset = 0
        
        await MainActor.run {
            if let index = transfers.firstIndex(where: { $0.id == transfer.id }) {
                transfers[index].status = .transferring
            }
        }
        
        while offset < data.count {
            let chunkEnd = min(offset + chunkSize, data.count)
            let chunk = data[offset..<chunkEnd]
            
            // TODO: Send chunk over network
            // networkManager.sendChunk(chunk, transferID: transfer.id)
            
            offset = chunkEnd
            let progress = Double(offset) / Double(data.count)
            
            await MainActor.run {
                if let index = transfers.firstIndex(where: { $0.id == transfer.id }) {
                    transfers[index].progress = progress
                }
                updateTotalProgress()
            }
            
            // Throttle for smooth progress
            try await Task.sleep(nanoseconds: 10_000_000) // 10ms
        }
        
        await MainActor.run {
            if let index = transfers.firstIndex(where: { $0.id == transfer.id }) {
                transfers[index].status = .completed
            }
        }
    }
    
    // MARK: - Receive File
    func receiveFile(fileName: String, data: Data) async throws {
        let transfer = FileTransfer(
            id: UUID(),
            fileName: fileName,
            fileSize: Int64(data.count),
            progress: 0,
            status: .receiving
        )
        
        await MainActor.run {
            transfers.append(transfer)
        }
        
        // Save to Downloads
        let downloadsURL = FileManager.default.urls(for: .downloadsDirectory, in: .userDomainMask)[0]
        let destinationURL = downloadsURL.appendingPathComponent(fileName)
        
        try data.write(to: destinationURL)
        
        await MainActor.run {
            if let index = transfers.firstIndex(where: { $0.id == transfer.id }) {
                transfers[index].status = .completed
                transfers[index].progress = 1.0
            }
        }
        
        // Show notification
        showNotification(title: "File Received", message: "Downloaded \(fileName)")
    }
    
    // MARK: - Cancel Transfer
    func cancelTransfer(_ transfer: FileTransfer) {
        if let index = transfers.firstIndex(where: { $0.id == transfer.id }) {
            transfers[index].status = .cancelled
        }
    }
    
    // MARK: - Clear Completed
    func clearCompleted() {
        transfers.removeAll { $0.status == .completed || $0.status == .cancelled }
    }
    
    // MARK: - Update Total Progress
    private func updateTotalProgress() {
        let activeTransfers = transfers.filter { $0.status == .transferring || $0.status == .receiving }
        if !activeTransfers.isEmpty {
            totalProgress = activeTransfers.map(\.progress).reduce(0, +) / Double(activeTransfers.count)
        } else {
            totalProgress = 0
        }
    }
    
    // MARK: - Show Notification
    private func showNotification(title: String, message: String) {
        let notification = NSUserNotification()
        notification.title = title
        notification.informativeText = message
        notification.soundName = NSUserNotificationDefaultSoundName
        NSUserNotificationCenter.default.deliver(notification)
    }
}

// MARK: - File Transfer Model
struct FileTransfer: Identifiable {
    let id: UUID
    let fileName: String
    let fileSize: Int64
    var progress: Double
    var status: Status
    
    enum Status {
        case preparing
        case transferring
        case receiving
        case completed
        case cancelled
        case failed
    }
    
    var formattedSize: String {
        ByteCountFormatter.string(fromByteCount: fileSize, countStyle: .file)
    }
}
