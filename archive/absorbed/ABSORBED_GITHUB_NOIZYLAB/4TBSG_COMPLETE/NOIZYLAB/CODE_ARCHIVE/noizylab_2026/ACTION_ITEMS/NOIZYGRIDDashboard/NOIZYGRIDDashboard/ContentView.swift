import SwiftUI

struct VM: Identifiable {
    let id = UUID()
    let name: String
    var status: String
}

struct ContentView: View {
    @State private var vmList: [VM] = []
    @State private var logOutput: String = "🧬 Ritual log will appear here..."

    var body: some View {
        VStack(spacing: 20) {
            Text("🧬 NOIZYGRID Dashboard")
                .font(.largeTitle)
                .padding()

            List(vmList) { vm in
                HStack {
                    Text(vm.name)
                    Spacer()
                    Text(vm.status)
                        .foregroundColor(vm.status == "running" ? .green : .red)
                    Button("Heal") { runCommand("noizy heal \(vm.name)") }
                    Button("Silence") { runCommand("noizy silence \(vm.name)") }
                    Button("Snapshot") { runCommand("noizy snapshot \(vm.name)") }
                }
            }

            HStack {
                Button("Sync Grid") { runCommand("noizy sync") }
                Button("Inject Branding") { runCommand("noizy inject wallpaper.jpg") }
                Button("Refresh Status") { refreshVMStatus() }
            }
            .padding()

            ScrollView {
                Text(logOutput)
                    .font(.system(.body, design: .monospaced))
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(Color.black.opacity(0.05))
                    .cornerRadius(8)
            }
            .frame(height: 200)
        }
        .padding()
        .onAppear {
            refreshVMStatus()
        }
        .frame(minWidth: 700, minHeight: 600)
    }

    func runCommand(_ command: String) {
        let task = Process()
        let pipe = Pipe()
        task.standardOutput = pipe
        task.standardError = pipe
        task.launchPath = "/bin/bash"
        task.arguments = ["-c", command]
        task.launch()

        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        let output = String(data: data, encoding: .utf8) ?? "No output"
        logOutput = "🔮 Command: \(command)\n\n\(output)"
    }

    func refreshVMStatus() {
        let task = Process()
        let pipe = Pipe()
        task.standardOutput = pipe
        task.launchPath = "/bin/bash"
        task.arguments = ["-c", "prlctl list --all | awk 'NR>1 {print $2, $4}'"]

        task.launch()
        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        let output = String(data: data, encoding: .utf8) ?? ""

        let lines = output.split(separator: "\n")
        vmList = lines.map { line in
            let parts = line.split(separator: " ")
            return VM(name: String(parts[0]), status: String(parts[1]))
        }
    }
}

@main
struct NoizyDashboardApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
