import Foundation
import ScreenCaptureKit
import AppKit

/// 🖥️🖥️🖥️ MULTI-DISPLAY SUPPORT - CAPTURE ALL SCREENS
@available(macOS 13.0, *)
class MultiDisplayManager: ObservableObject {
    @Published var displays: [DisplayInfo] = []
    @Published var selectedDisplayID: String?
    
    // MARK: - Discover Displays
    func discoverDisplays() async {
        do {
            let content = try await SCShareableContent.excludingDesktopWindows(
                false,
                onScreenWindowsOnly: false
            )
            
            let displayInfos = content.displays.map { display in
                DisplayInfo(
                    id: display.displayID.description,
                    name: getDisplayName(for: display),
                    width: display.width,
                    height: display.height,
                    frame: display.frame,
                    isPrimary: display.displayID == CGMainDisplayID()
                )
            }
            
            await MainActor.run {
                displays = displayInfos
                if selectedDisplayID == nil {
                    selectedDisplayID = displayInfos.first(where: { $0.isPrimary })?.id
                }
            }
        } catch {
            print("❌ Failed to discover displays: \(error)")
        }
    }
    
    // MARK: - Get Display Name
    private func getDisplayName(for display: SCDisplay) -> String {
        let screens = NSScreen.screens
        if let screen = screens.first(where: { $0.displayID == display.displayID }) {
            return screen.localizedName
        }
        return "Display \(display.displayID)"
    }
    
    // MARK: - Select Display
    func selectDisplay(_ id: String) {
        selectedDisplayID = id
    }
}

// MARK: - Display Info
struct DisplayInfo: Identifiable, Hashable {
    let id: String
    let name: String
    let width: Int
    let height: Int
    let frame: CGRect
    let isPrimary: Bool
    
    var resolution: String {
        "\(width) × \(height)"
    }
    
    var aspectRatio: String {
        let gcd = greatestCommonDivisor(width, height)
        let w = width / gcd
        let h = height / gcd
        return "\(w):\(h)"
    }
    
    private func greatestCommonDivisor(_ a: Int, _ b: Int) -> Int {
        return b == 0 ? a : greatestCommonDivisor(b, a % b)
    }
}

// MARK: - NSScreen Extension
extension NSScreen {
    var displayID: CGDirectDisplayID {
        let key = NSDeviceDescriptionKey("NSScreenNumber")
        return deviceDescription[key] as? CGDirectDisplayID ?? 0
    }
}
