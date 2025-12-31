//
//  MC96ECOUNIVERSEApp.swift
//  MC96ECOUNIVERSE
//
//  Created by M2Ultra on 2025-12-18.
//

import SwiftUI
import SwiftData

@main
struct MC96ECOUNIVERSEApp: App {
    var sharedModelContainer: ModelContainer = {
        let schema = Schema([
            Item.self,
        ])
        let modelConfiguration = ModelConfiguration(schema: schema, isStoredInMemoryOnly: false)

        do {
            return try ModelContainer(for: schema, configurations: [modelConfiguration])
        } catch {
            fatalError("Could not create ModelContainer: \(error)")
        }
    }()

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(sharedModelContainer)
    }
}
