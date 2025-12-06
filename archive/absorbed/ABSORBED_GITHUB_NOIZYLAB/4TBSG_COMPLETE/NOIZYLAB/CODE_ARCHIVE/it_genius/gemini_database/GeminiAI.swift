//
// GeminiAI.swift
// Gemini AI Integration for iOS
//

import Foundation

class GeminiAI {
    private let apiKey: String
    private let baseURL = "https://generativelanguage.googleapis.com/v1beta"
    
    init(apiKey: String) {
        self.apiKey = apiKey
    }
    
    func generateText(prompt: String, model: String = "gemini-pro") async throws -> String {
        let url = URL(string: "\(baseURL)/models/\(model):generateContent?key=\(apiKey)")!
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let body: [String: Any] = [
            "contents": [[
                "parts": [["text": prompt]]
            ]]
        ]
        
        request.httpBody = try JSONSerialization.data(withJSONObject: body)
        
        let (data, _) = try await URLSession.shared.data(for: request)
        let response = try JSONDecoder().decode(GeminiResponse.self, from: data)
        
        return response.candidates[0].content.parts[0].text
    }
    
    func solveProblem(_ problem: String) async throws -> String {
        let prompt = """
        You are an expert IT repair technician. Solve this problem:
        
        \(problem)
        
        Provide:
        1. Diagnosis
        2. Step-by-step solution
        3. Alternative solutions
        4. Prevention tips
        """
        
        return try await generateText(prompt: prompt)
    }
}

struct GeminiResponse: Codable {
    let candidates: [Candidate]
    
    struct Candidate: Codable {
        let content: Content
    }
    
    struct Content: Codable {
        let parts: [Part]
    }
    
    struct Part: Codable {
        let text: String
    }
}
