import Foundation
import AVFoundation
import CoreImage

/// 🎥 SESSION RECORDING - RECORD EVERYTHING FOR AUDIT
class RecordingManager: ObservableObject {
    @Published var isRecording = false
    @Published var recordingDuration: TimeInterval = 0
    @Published var recordingSize: Int64 = 0
    
    private var writer: AVAssetWriter?
    private var videoInput: AVAssetWriterInput?
    private var adaptor: AVAssetWriterInputPixelBufferAdaptor?
    private var startTime: Date?
    private var frameCount: Int = 0
    
    // MARK: - Start Recording
    func startRecording(sessionID: String, size: CGSize) throws {
        guard !isRecording else { return }
        
        // Create output URL
        let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        let recordingsPath = documentsPath.appendingPathComponent("NoizyLabRecordings")
        try FileManager.default.createDirectory(at: recordingsPath, withIntermediateDirectories: true)
        
        let filename = "Session_\(sessionID)_\(Date().timeIntervalSince1970).mp4"
        let outputURL = recordingsPath.appendingPathComponent(filename)
        
        // Create asset writer
        writer = try AVAssetWriter(url: outputURL, fileType: .mp4)
        
        // Video settings
        let videoSettings: [String: Any] = [
            AVVideoCodecKey: AVVideoCodecType.h264,
            AVVideoWidthKey: size.width,
            AVVideoHeightKey: size.height,
            AVVideoCompressionPropertiesKey: [
                AVVideoAverageBitRateKey: 5_000_000, // 5 Mbps
                AVVideoMaxKeyFrameIntervalKey: 30,
                AVVideoProfileLevelKey: AVVideoProfileLevelH264HighAutoLevel
            ]
        ]
        
        // Create video input
        videoInput = AVAssetWriterInput(mediaType: .video, outputSettings: videoSettings)
        videoInput?.expectsMediaDataInRealTime = true
        
        // Create pixel buffer adaptor
        let sourcePixelBufferAttributes: [String: Any] = [
            kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA,
            kCVPixelBufferWidthKey as String: size.width,
            kCVPixelBufferHeightKey as String: size.height,
        ]
        
        adaptor = AVAssetWriterInputPixelBufferAdaptor(
            assetWriterInput: videoInput!,
            sourcePixelBufferAttributes: sourcePixelBufferAttributes
        )
        
        // Add input to writer
        if let videoInput = videoInput, writer?.canAdd(videoInput) == true {
            writer?.add(videoInput)
        }
        
        // Start writing
        writer?.startWriting()
        writer?.startSession(atSourceTime: .zero)
        
        startTime = Date()
        isRecording = true
        frameCount = 0
        
        print("🎥 Recording started: \(filename)")
    }
    
    // MARK: - Add Frame
    func addFrame(_ cgImage: CGImage) {
        guard isRecording,
              let adaptor = adaptor,
              let videoInput = videoInput,
              videoInput.isReadyForMoreMediaData else { return }
        
        // Create pixel buffer from CGImage
        var pixelBuffer: CVPixelBuffer?
        let attrs = [
            kCVPixelBufferCGImageCompatibilityKey: kCFBooleanTrue,
            kCVPixelBufferCGBitmapContextCompatibilityKey: kCFBooleanTrue
        ] as CFDictionary
        
        CVPixelBufferCreate(
            kCFAllocatorDefault,
            cgImage.width,
            cgImage.height,
            kCVPixelFormatType_32BGRA,
            attrs,
            &pixelBuffer
        )
        
        guard let pixelBuffer = pixelBuffer else { return }
        
        // Fill pixel buffer with image data
        CVPixelBufferLockBaseAddress(pixelBuffer, [])
        let context = CGContext(
            data: CVPixelBufferGetBaseAddress(pixelBuffer),
            width: cgImage.width,
            height: cgImage.height,
            bitsPerComponent: 8,
            bytesPerRow: CVPixelBufferGetBytesPerRow(pixelBuffer),
            space: CGColorSpaceCreateDeviceRGB(),
            bitmapInfo: CGImageAlphaInfo.premultipliedFirst.rawValue
        )
        context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: cgImage.width, height: cgImage.height))
        CVPixelBufferUnlockBaseAddress(pixelBuffer, [])
        
        // Calculate presentation time
        let elapsed = Date().timeIntervalSince(startTime ?? Date())
        let presentationTime = CMTime(seconds: elapsed, preferredTimescale: 600)
        
        // Append pixel buffer
        adaptor.append(pixelBuffer, withPresentationTime: presentationTime)
        
        frameCount += 1
        recordingDuration = elapsed
        
        // Update file size
        if let writer = writer, let url = writer.outputURL {
            if let attrs = try? FileManager.default.attributesOfItem(atPath: url.path) {
                recordingSize = attrs[.size] as? Int64 ?? 0
            }
        }
    }
    
    // MARK: - Stop Recording
    func stopRecording() async {
        guard isRecording else { return }
        
        isRecording = false
        
        videoInput?.markAsFinished()
        
        await writer?.finishWriting()
        
        if let url = writer?.outputURL {
            print("🎥 Recording saved: \(url.path)")
            print("   Duration: \(recordingDuration)s")
            print("   Frames: \(frameCount)")
            print("   Size: \(ByteCountFormatter.string(fromByteCount: recordingSize, countStyle: .file))")
            
            // Show notification
            showNotification(url: url)
        }
        
        writer = nil
        videoInput = nil
        adaptor = nil
    }
    
    // MARK: - Show Notification
    private func showNotification(url: URL) {
        let notification = NSUserNotification()
        notification.title = "Recording Saved"
        notification.informativeText = "Session recording saved to Documents"
        notification.soundName = NSUserNotificationDefaultSoundName
        notification.userInfo = ["url": url.path]
        NSUserNotificationCenter.default.deliver(notification)
    }
    
    // MARK: - Format Duration
    var formattedDuration: String {
        let minutes = Int(recordingDuration) / 60
        let seconds = Int(recordingDuration) % 60
        return String(format: "%02d:%02d", minutes, seconds)
    }
    
    var formattedSize: String {
        ByteCountFormatter.string(fromByteCount: recordingSize, countStyle: .file)
    }
}
