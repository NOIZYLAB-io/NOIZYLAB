import Foundation
import ScreenCaptureKit
import CoreImage

/// 🔥 REAL-TIME SCREEN CAPTURE - NO MORE DEMO SHIT!
@available(macOS 13.0, *)
class ScreenCaptureManager: NSObject, ObservableObject {
    @Published var capturedImage: CGImage?
    @Published var isCapturing = false
    @Published var fps: Int = 0
    
    private var stream: SCStream?
    private var frameCount = 0
    private var lastFPSUpdate = Date()
    
    // MARK: - Start Capture
    func startCapture(for displayID: String? = nil) async throws {
        guard !isCapturing else { return }
        
        // Get available content
        let content = try await SCShareableContent.excludingDesktopWindows(
            false,
            onScreenWindowsOnly: true
        )
        
        // Select display
        guard let display = displayID != nil 
            ? content.displays.first(where: { $0.displayID.description == displayID })
            : content.displays.first 
        else {
            throw CaptureError.noDisplayFound
        }
        
        // Create filter (capture entire display)
        let filter = SCContentFilter(display: display, excludingWindows: [])
        
        // Configure stream for HIGH QUALITY
        let config = SCStreamConfiguration()
        config.width = display.width * 2  // Retina
        config.height = display.height * 2
        config.minimumFrameInterval = CMTime(value: 1, timescale: 60) // 60 FPS
        config.queueDepth = 6
        config.pixelFormat = kCVPixelFormatType_32BGRA
        config.showsCursor = true
        config.backgroundColor = .clear
        
        // Create stream
        stream = SCStream(filter: filter, configuration: config, delegate: self)
        
        // Add stream output
        try stream?.addStreamOutput(self, type: .screen, sampleHandlerQueue: .global(qos: .userInteractive))
        
        // Start capture
        try await stream?.startCapture()
        
        await MainActor.run {
            isCapturing = true
        }
    }
    
    // MARK: - Stop Capture
    func stopCapture() async throws {
        guard isCapturing else { return }
        
        try await stream?.stopCapture()
        stream = nil
        
        await MainActor.run {
            isCapturing = false
            capturedImage = nil
        }
    }
    
    enum CaptureError: Error {
        case noDisplayFound
        case captureNotStarted
    }
}

// MARK: - SCStreamDelegate
@available(macOS 13.0, *)
extension ScreenCaptureManager: SCStreamDelegate {
    func stream(_ stream: SCStream, didStopWithError error: Error) {
        print("❌ Screen capture stopped with error: \(error.localizedDescription)")
        Task { @MainActor in
            isCapturing = false
        }
    }
}

// MARK: - SCStreamOutput
@available(macOS 13.0, *)
extension ScreenCaptureManager: SCStreamOutput {
    func stream(_ stream: SCStream, didOutputSampleBuffer sampleBuffer: CMSampleBuffer, of type: SCStreamOutputType) {
        guard type == .screen,
              let imageBuffer = sampleBuffer.imageBuffer else { return }
        
        // Create CGImage from CVPixelBuffer
        let ciImage = CIImage(cvPixelBuffer: imageBuffer)
        let context = CIContext(options: nil)
        
        if let cgImage = context.createCGImage(ciImage, from: ciImage.extent) {
            Task { @MainActor in
                capturedImage = cgImage
                
                // Calculate FPS
                frameCount += 1
                let now = Date()
                if now.timeIntervalSince(lastFPSUpdate) >= 1.0 {
                    fps = frameCount
                    frameCount = 0
                    lastFPSUpdate = now
                }
            }
        }
    }
}
