// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "NoizyLabStatus",
    platforms: [
        .macOS(.v13)
    ],
    products: [
        .executable(name: "NoizyLabStatus", targets: ["NoizyLabStatus"])
    ],
    targets: [
        .executableTarget(
            name: "NoizyLabStatus",
            path: "Sources"
        )
    ]
)
