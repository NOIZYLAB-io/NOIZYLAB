import Foundation
import AppKit
import Carbon

/// ⌨️ KEYBOARD SHORTCUTS - POWER USER FEATURES
class KeyboardShortcutsManager {
    private var eventMonitor: Any?
    
    // Callback handlers
    var onScreenshot: (() -> Void)?
    var onToggleChat: (() -> Void)?
    var onToggleFullscreen: (() -> Void)?
    var onDisconnect: (() -> Void)?
    var onToggleRecording: (() -> Void)?
    
    // MARK: - Start Monitoring
    func startMonitoring() {
        eventMonitor = NSEvent.addLocalMonitorForEvents(matching: .keyDown) { [weak self] event in
            return self?.handleKeyEvent(event) ?? event
        }
    }
    
    // MARK: - Stop Monitoring
    func stopMonitoring() {
        if let monitor = eventMonitor {
            NSEvent.removeMonitor(monitor)
            eventMonitor = nil
        }
    }
    
    // MARK: - Handle Key Event
    private func handleKeyEvent(_ event: NSEvent) -> NSEvent? {
        let flags = event.modifierFlags
        let keyCode = event.keyCode
        
        // ⌘⇧S - Screenshot
        if flags.contains([.command, .shift]) && keyCode == kVK_ANSI_S {
            onScreenshot?()
            return nil
        }
        
        // ⌘⇧C - Toggle Chat
        if flags.contains([.command, .shift]) && keyCode == kVK_ANSI_C {
            onToggleChat?()
            return nil
        }
        
        // ⌘⇧F - Toggle Fullscreen
        if flags.contains([.command, .shift]) && keyCode == kVK_ANSI_F {
            onToggleFullscreen?()
            return nil
        }
        
        // ⌘Q - Disconnect (override default quit)
        if flags.contains(.command) && keyCode == kVK_ANSI_Q {
            onDisconnect?()
            return nil
        }
        
        // ⌘R - Toggle Recording
        if flags.contains(.command) && keyCode == kVK_ANSI_R {
            onToggleRecording?()
            return nil
        }
        
        return event
    }
}

// MARK: - Shortcut Info
struct KeyboardShortcut {
    let keys: String
    let description: String
    
    static let allShortcuts = [
        KeyboardShortcut(keys: "⌘⇧S", description: "Take Screenshot"),
        KeyboardShortcut(keys: "⌘⇧C", description: "Toggle Chat"),
        KeyboardShortcut(keys: "⌘⇧F", description: "Toggle Fullscreen"),
        KeyboardShortcut(keys: "⌘R", description: "Toggle Recording"),
        KeyboardShortcut(keys: "⌘Q", description: "Disconnect"),
        KeyboardShortcut(keys: "⌘,", description: "Preferences"),
    ]
}
