//
// NOIZYLABApp.swift
// NOIZYLAB iOS App
//

import SwiftUI

@main
struct NOIZYLABApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                Text("🚀 NOIZYLAB")
                    .font(.largeTitle)
                    .padding()
                
                List {
                    NavigationLink("Problem Solver", destination: ProblemSolverView())
                    NavigationLink("AI Trainer", destination: AITrainerView())
                    NavigationLink("Analytics", destination: AnalyticsView())
                    NavigationLink("Monitoring", destination: MonitoringView())
                }
            }
            .navigationTitle("NOIZYLAB")
        }
    }
}

struct ProblemSolverView: View {
    var body: some View {
        Text("Problem Solver")
            .navigationTitle("Problem Solver")
    }
}

struct AITrainerView: View {
    var body: some View {
        Text("AI Trainer")
            .navigationTitle("AI Trainer")
    }
}

struct AnalyticsView: View {
    var body: some View {
        Text("Analytics")
            .navigationTitle("Analytics")
    }
}

struct MonitoringView: View {
    var body: some View {
        Text("Monitoring")
            .navigationTitle("Monitoring")
    }
}
