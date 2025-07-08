from pydub.utils import mediainfo
import os

folder_path = "D:/Minor project - Dialect AI/making-datasets/Datasets/Sad"  # Change this

total_duration = 0  # in seconds

for filename in os.listdir(folder_path):
    if filename.endswith(".mp3") or filename.endswith(".wav"):  # add other formats if needed
        info = mediainfo(os.path.join(folder_path, filename))
        duration = float(info['duration'])
        total_duration += duration

minutes, seconds = divmod(int(total_duration), 60)
hours, minutes = divmod(minutes, 60)

print(f"Total Duration: {hours}h {minutes}m {seconds}s")
