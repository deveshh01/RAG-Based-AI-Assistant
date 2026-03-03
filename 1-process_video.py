import os
import subprocess

VIDEO_FOLDER = "videos"
OUTPUT_FOLDER = "audio"

# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(VIDEO_FOLDER):
    if file.endswith(".mp4"):
        video_path = os.path.join(VIDEO_FOLDER, file)
        
        # Change extension to .mp3
        output_file = file.replace(".mp4", ".mp3")
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        command = [
            "ffmpeg",
            "-i", video_path,
            "-q:a", "0",
            "-map", "a",
            output_path
        ]

        print(f"Converting {file} → {output_file}")
        subprocess.run(command)

print("All MP4 files converted successfully 🚀")