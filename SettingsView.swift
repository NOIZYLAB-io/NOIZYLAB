import SwiftUI

struct SettingsView: View {
    @AppStorage("enableLogging") private var enableLogging = true
    @AppStorage("enableNotifications") private var enableNotifications = true
    @AppStorage("autoConnect") private var autoConnect = false
    
    var body: some View {
        TabView {
            // General settings
            Form {
                Section(header: Text("General")) {
                    Toggle("Enable Session Logging", isOn: $enableLogging)
                    Toggle("Enable Notifications", isOn: $enableNotifications)
                    Toggle("Auto-connect on launch", isOn: $autoConnect)
                }
                
                Section(header: Text("About")) {
                    HStack {
                        Text("Version")
                        Spacer()
                        Text("1.0.0")
                            .foregroundColor(.secondary)
                    }
                    
                    HStack {
                        Text("Build")
                        Spacer()
                        Text("2025.12.01")
                            .foregroundColor(.secondary)
                    }
                    
                    Divider()
                    
                    Text("NOIZYLAB Remote Access")
                        .font(.headline)
                    Text("Fish Music Inc - CB_01")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    Text("🔥 GORUNFREE! 🎸🔥")
                        .font(.caption2)
                        .foregroundColor(.pink)
                }
            }
            .padding()
            .frame(width: 500, height: 400)
            .tabItem {
                Label("General", systemImage: "gear")
            }
        }
    }
}
