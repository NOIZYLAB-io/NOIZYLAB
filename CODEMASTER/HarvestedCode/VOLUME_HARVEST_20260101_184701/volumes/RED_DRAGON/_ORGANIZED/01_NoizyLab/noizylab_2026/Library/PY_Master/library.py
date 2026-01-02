class AudioLibrary:
    def __init__(self, paths):
        self.paths = paths
        self.audio_files = []

    def scan_audio_files(self):
        # Logic to scan specified paths for audio files
        pass

    def deduplicate_audio_files(self):
        # Logic to deduplicate entries based on checksums
        pass

    def export_to_csv(self, output_path):
        # Logic to export the audio library to CSV format
        pass

    def export_to_yaml(self, output_path):
        # Logic to export the audio library to YAML format
        pass