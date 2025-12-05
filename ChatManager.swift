import Foundation
import Combine

/// 💬 BUILT-IN CHAT - TALK DURING REMOTE SESSION
class ChatManager: ObservableObject {
    @Published var messages: [ChatMessage] = []
    @Published var unreadCount: Int = 0
    
    private let currentUser: String
    
    init(currentUser: String = NSFullUserName()) {
        self.currentUser = currentUser
    }
    
    // MARK: - Send Message
    func sendMessage(_ text: String, to recipient: String) {
        let message = ChatMessage(
            id: UUID(),
            text: text,
            sender: currentUser,
            recipient: recipient,
            timestamp: Date(),
            isRead: false,
            isSentByMe: true
        )
        
        messages.append(message)
        
        // TODO: Send over network
        // networkManager.sendChatMessage(message)
    }
    
    // MARK: - Receive Message
    func receiveMessage(text: String, from sender: String) {
        let message = ChatMessage(
            id: UUID(),
            text: text,
            sender: sender,
            recipient: currentUser,
            timestamp: Date(),
            isRead: false,
            isSentByMe: false
        )
        
        messages.append(message)
        unreadCount += 1
        
        // Show notification
        showNotification(from: sender, text: text)
    }
    
    // MARK: - Mark as Read
    func markAsRead() {
        for index in messages.indices where !messages[index].isRead && !messages[index].isSentByMe {
            messages[index].isRead = true
        }
        unreadCount = 0
    }
    
    // MARK: - Clear History
    func clearHistory() {
        messages.removeAll()
        unreadCount = 0
    }
    
    // MARK: - Show Notification
    private func showNotification(from sender: String, text: String) {
        let notification = NSUserNotification()
        notification.title = "Message from \(sender)"
        notification.informativeText = text
        notification.soundName = NSUserNotificationDefaultSoundName
        NSUserNotificationCenter.default.deliver(notification)
    }
}

// MARK: - Chat Message Model
struct ChatMessage: Identifiable {
    let id: UUID
    let text: String
    let sender: String
    let recipient: String
    let timestamp: Date
    var isRead: Bool
    let isSentByMe: Bool
    
    var formattedTime: String {
        let formatter = DateFormatter()
        formatter.dateFormat = "HH:mm"
        return formatter.string(from: timestamp)
    }
}
