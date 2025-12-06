// Swift AI Integration Examples

// core_ml_example

import CoreML
import Vision

// Load model
guard let model = try? VNCoreMLModel(for: YourModel().model) else {
    return
}

// Create request
let request = VNCoreMLRequest(model: model) { request, error in
    guard let results = request.results as? [VNClassificationObservation] else {
        return
    }
    // Handle results
}

// Perform request
let handler = VNImageRequestHandler(ciImage: image)
try? handler.perform([request])


// openai_api_example

import Foundation

func callOpenAI(prompt: String) async throws -> String {
    let url = URL(string: "https://api.openai.com/v1/chat/completions")!
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    request.setValue("Bearer YOUR_API_KEY", forHTTPHeaderField: "Authorization")
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")
    
    let body: [String: Any] = [
        "model": "gpt-4",
        "messages": [["role": "user", "content": prompt]]
    ]
    request.httpBody = try JSONSerialization.data(withJSONObject: body)
    
    let (data, _) = try await URLSession.shared.data(for: request)
    let response = try JSONDecoder().decode(OpenAIResponse.self, from: data)
    return response.choices[0].message.content
}


// vision_example

import Vision

func recognizeText(in image: UIImage) {
    guard let cgImage = image.cgImage else { return }
    
    let request = VNRecognizeTextRequest { request, error in
        guard let observations = request.results as? [VNRecognizedTextObservation] else {
            return
        }
        for observation in observations {
            guard let topCandidate = observation.topCandidates(1).first else {
                continue
            }
            print(topCandidate.string)
        }
    }
    
    let handler = VNImageRequestHandler(cgImage: cgImage)
    try? handler.perform([request])
}


