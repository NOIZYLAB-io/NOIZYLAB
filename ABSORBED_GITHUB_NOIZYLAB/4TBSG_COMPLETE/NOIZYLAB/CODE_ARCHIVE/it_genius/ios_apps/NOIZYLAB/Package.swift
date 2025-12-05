// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "NOIZYLAB",
    platforms: [
        .iOS(.v15)
    ],
    products: [
        .library(
            name: "NOIZYLAB",
            targets: ["NOIZYLAB"]),
    ],
    targets: [
        .target(
            name: "NOIZYLAB",
            dependencies: [])
    ]
)

