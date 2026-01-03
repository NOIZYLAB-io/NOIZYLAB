import SwiftUI
import AppKit

@main
struct NoizyLabStatusApp: App {
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    var body: some Scene {
        Settings {
            EmptyView()
        }
    }
}

class AppDelegate: NSObject, NSApplicationDelegate {
    var statusItem: NSStatusItem?
    var popover: NSPopover?
    
    func applicationDidFinishLaunching(_ notification: Notification) {
        setupMenuBar()
    }
    
    func setupMenuBar() {
        statusItem = NSStatusBar.system.statusItem(withLength: NSStatusItem.variableLength)
        
        if let button = statusItem?.button {
            button.image = NSImage(systemSymbolName: "brain.head.profile", accessibilityDescription: "NoizyLab OS")
            button.title = " 57"
            button.action = #selector(togglePopover)
        }
        
        popover = NSPopover()
        popover?.contentSize = NSSize(width: 320, height: 400)
        popover?.behavior = .transient
        popover?.contentViewController = NSHostingController(rootView: NoizyLabPopoverView())
    }
    
    @objc func togglePopover() {
        if let button = statusItem?.button {
            if popover?.isShown == true {
                popover?.performClose(nil)
            } else {
                popover?.show(relativeTo: button.bounds, of: button, preferredEdge: .minY)
            }
        }
    }
}

struct NoizyLabPopoverView: View {
    @State private var workerCount = 57
    @State private var isDeploying = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Header
            HStack {
                Text("🧠")
                    .font(.system(size: 32))
                VStack(alignment: .leading) {
                    Text("NoizyLab OS")
                        .font(.headline)
                        .fontWeight(.bold)
                    Text("Omni-Sovereign AI Platform")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                Spacer()
            }
            
            Divider()
            
            // Stats Grid
            HStack(spacing: 12) {
                StatBox(value: "57", label: "Workers", color: .green)
                StatBox(value: "21", label: "Round 3", color: .yellow)
                StatBox(value: "3", label: "Rounds", color: .blue)
            }
            
            // Status
            HStack {
                Circle()
                    .fill(Color.green)
                    .frame(width: 8, height: 8)
                Text("All Systems Operational")
                    .font(.caption)
                    .foregroundColor(.green)
                Spacer()
            }
            .padding(10)
            .background(Color.green.opacity(0.1))
            .cornerRadius(8)
            
            Divider()
            
            // Worker Categories
            Text("Worker Categories")
                .font(.caption)
                .foregroundColor(.secondary)
            
            ScrollView {
                VStack(alignment: .leading, spacing: 8) {
                    WorkerRow(icon: "🏗️", name: "Core Infrastructure", count: 5)
                    WorkerRow(icon: "💼", name: "Business Logic", count: 4)
                    WorkerRow(icon: "🔧", name: "Technician Support", count: 5)
                    WorkerRow(icon: "🧠", name: "Round 1: Genius AI", count: 9)
                    WorkerRow(icon: "🚀", name: "Round 2: Next-Gen", count: 10)
                    WorkerRow(icon: "🏆", name: "Round 3: Legends", count: 20)
                    WorkerRow(icon: "🎯", name: "Orchestration", count: 3)
                }
            }
            .frame(maxHeight: 150)
            
            Divider()
            
            // Actions
            HStack {
                Button(action: deploy) {
                    HStack {
                        if isDeploying {
                            ProgressView()
                                .scaleEffect(0.7)
                        } else {
                            Image(systemName: "arrow.up.circle.fill")
                        }
                        Text("Deploy")
                    }
                }
                .buttonStyle(.borderedProminent)
                .disabled(isDeploying)
                
                Button(action: openTerminal) {
                    HStack {
                        Image(systemName: "terminal.fill")
                        Text("CLI")
                    }
                }
                .buttonStyle(.bordered)
                
                Spacer()
                
                Button(action: quit) {
                    Image(systemName: "xmark.circle")
                }
                .buttonStyle(.plain)
            }
        }
        .padding()
        .frame(width: 320)
    }
    
    func deploy() {
        isDeploying = true
        let task = Process()
        task.launchPath = "/bin/zsh"
        task.arguments = ["-c", "cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && ./deploy.sh deploy"]
        task.launch()
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            isDeploying = false
        }
    }
    
    func openTerminal() {
        let script = """
        tell application "Terminal"
            activate
            do script "cd /Users/m2ultra/NOIZYLAB/GABRIEL/noizylab-os && nl --help"
        end tell
        """
        var error: NSDictionary?
        NSAppleScript(source: script)?.executeAndReturnError(&error)
    }
    
    func quit() {
        NSApplication.shared.terminate(nil)
    }
}

struct StatBox: View {
    let value: String
    let label: String
    let color: Color
    
    var body: some View {
        VStack(spacing: 4) {
            Text(value)
                .font(.title)
                .fontWeight(.bold)
                .foregroundColor(color)
            Text(label)
                .font(.caption2)
                .foregroundColor(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding(12)
        .background(color.opacity(0.1))
        .cornerRadius(8)
    }
}

struct WorkerRow: View {
    let icon: String
    let name: String
    let count: Int
    
    var body: some View {
        HStack {
            Text(icon)
            Text(name)
                .font(.caption)
            Spacer()
            Text("\(count)")
                .font(.caption)
                .foregroundColor(.secondary)
                .padding(.horizontal, 8)
                .padding(.vertical, 2)
                .background(Color.secondary.opacity(0.2))
                .cornerRadius(4)
        }
    }
}
