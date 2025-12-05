import platform


class PlatformDetector:
    @staticmethod
    def is_amd86() -> bool:
        return "i386" in platform.processor().lower()

    @staticmethod
    def is_amd64() -> bool:
        return (
            "x86_64" in platform.processor().lower()
            or "amd64" in platform.processor().lower()
            or "intel64" in platform.processor().lower()
        )

    @staticmethod
    def is_aarch64() -> bool:
        return "aarch64" in platform.processor().lower()

    @staticmethod
    def is_arm86() -> bool:
        return "arm" in platform.processor().lower() and not PlatformDetector.is_arm64()

    @staticmethod
    def is_arm64() -> bool:
        return (
            "arm" in platform.processor().lower() and "64" in platform.machine().lower()
        )

    @staticmethod
    def is_arm() -> bool:
        return "arm" in platform.processor().lower()

    @staticmethod
    def is_amd() -> bool:
        return (
            "x86" in platform.processor().lower()
            or "amd" in platform.processor().lower()
        )

    @staticmethod
    def get_arch_name() -> str:
        return platform.processor().lower()

    @staticmethod
    def is_windows() -> bool:
        return platform.system().lower() == "windows"

    @staticmethod
    def is_linux() -> bool:
        return platform.system().lower() == "linux"

    @staticmethod
    def is_darwin() -> bool:
        return platform.system().lower() == "darwin"

    @staticmethod
    def is_macos() -> bool:
        return PlatformDetector.is_darwin()

    @staticmethod
    def get_os_name() -> str:
        return platform.system().lower()

    @staticmethod
    def is_snapdragon_arm() -> bool:
        is_snapdragon = "qualcomm" in platform.processor().lower()
        return PlatformDetector.is_arm() and is_snapdragon
