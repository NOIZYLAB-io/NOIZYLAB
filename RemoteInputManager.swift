import Foundation
import CoreGraphics
import AppKit

/// 🎮 REMOTE INPUT CONTROL - KEYBOARD & MOUSE
class RemoteInputManager {
    
    // MARK: - Mouse Control
    func moveMouse(to point: CGPoint) {
        CGEvent(mouseEventSource: nil, mouseType: .mouseMoved, mouseCursorPosition: point, mouseButton: .left)?.post(tap: .cghidEventTap)
    }
    
    func clickMouse(at point: CGPoint, button: CGMouseButton = .left) {
        // Move to position
        moveMouse(to: point)
        
        // Mouse down
        CGEvent(mouseEventSource: nil, mouseType: .leftMouseDown, mouseCursorPosition: point, mouseButton: button)?.post(tap: .cghidEventTap)
        
        // Mouse up
        CGEvent(mouseEventSource: nil, mouseType: .leftMouseUp, mouseCursorPosition: point, mouseButton: button)?.post(tap: .cghidEventTap)
    }
    
    func doubleClick(at point: CGPoint) {
        clickMouse(at: point)
        usleep(100000) // 100ms delay
        clickMouse(at: point)
    }
    
    func rightClick(at point: CGPoint) {
        moveMouse(to: point)
        CGEvent(mouseEventSource: nil, mouseType: .rightMouseDown, mouseCursorPosition: point, mouseButton: .right)?.post(tap: .cghidEventTap)
        CGEvent(mouseEventSource: nil, mouseType: .rightMouseUp, mouseCursorPosition: point, mouseButton: .right)?.post(tap: .cghidEventTap)
    }
    
    func scroll(deltaY: Int32, at point: CGPoint) {
        moveMouse(to: point)
        CGEvent(scrollWheelEvent2Source: nil, units: .pixel, wheelCount: 1, wheel1: deltaY, wheel2: 0, wheel3: 0)?.post(tap: .cghidEventTap)
    }
    
    // MARK: - Keyboard Control
    func typeKey(_ key: CGKeyCode, modifiers: CGEventFlags = []) {
        // Key down
        if let keyDown = CGEvent(keyboardEventSource: nil, virtualKey: key, keyDown: true) {
            keyDown.flags = modifiers
            keyDown.post(tap: .cghidEventTap)
        }
        
        // Key up
        if let keyUp = CGEvent(keyboardEventSource: nil, virtualKey: key, keyDown: false) {
            keyUp.post(tap: .cghidEventTap)
        }
    }
    
    func typeString(_ text: String) {
        for char in text {
            if let keyCode = char.keyCode {
                typeKey(keyCode)
                usleep(50000) // 50ms delay between keys
            }
        }
    }
    
    // MARK: - Shortcuts
    func commandKey(_ key: CGKeyCode) {
        typeKey(key, modifiers: .maskCommand)
    }
    
    func controlKey(_ key: CGKeyCode) {
        typeKey(key, modifiers: .maskControl)
    }
    
    func optionKey(_ key: CGKeyCode) {
        typeKey(key, modifiers: .maskAlternate)
    }
    
    func shiftKey(_ key: CGKeyCode) {
        typeKey(key, modifiers: .maskShift)
    }
}

// MARK: - Character to KeyCode Mapping
extension Character {
    var keyCode: CGKeyCode? {
        switch self.lowercased() {
        case "a": return 0x00
        case "b": return 0x0B
        case "c": return 0x08
        case "d": return 0x02
        case "e": return 0x0E
        case "f": return 0x03
        case "g": return 0x05
        case "h": return 0x04
        case "i": return 0x22
        case "j": return 0x26
        case "k": return 0x28
        case "l": return 0x25
        case "m": return 0x2E
        case "n": return 0x2D
        case "o": return 0x1F
        case "p": return 0x23
        case "q": return 0x0C
        case "r": return 0x0F
        case "s": return 0x01
        case "t": return 0x11
        case "u": return 0x20
        case "v": return 0x09
        case "w": return 0x0D
        case "x": return 0x07
        case "y": return 0x10
        case "z": return 0x06
        case "0": return 0x1D
        case "1": return 0x12
        case "2": return 0x13
        case "3": return 0x14
        case "4": return 0x15
        case "5": return 0x17
        case "6": return 0x16
        case "7": return 0x1A
        case "8": return 0x1C
        case "9": return 0x19
        case " ": return 0x31  // Space
        case "\n": return 0x24 // Return
        default: return nil
        }
    }
}
