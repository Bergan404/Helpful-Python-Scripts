import os
import sys
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# listdir returs a list of all the names within the file, doesnt print it but it shows them
# entries = os.listdir('/Users/berganoudshoorn/Downloads/')

# Using a for loop to itterate through all the listiings and print them as strings
# for entry in entries:
#  print(entry)

# source directory also my downloads directory
source = '/Users/berganoudshoorn/Downloads/'
image_directory = '/Users/berganoudshoorn/Downloads/Images'
video_directory = '/Users/berganoudshoorn/Downloads/Videos'
documents_directory = '/Users/berganoudshoorn/Downloads/Documents'
audio_directory = '/Users/berganoudshoorn/Downloads/Audio'
other_directory = '/Users/berganoudshoorn/Downloads/Other'

class FileHandler(FileSystemEventHandler):
    def organize_existing_files(self):
        for filename in os.listdir(source):
            src_file = os.path.join(source, filename)
            if os.path.isfile(src_file):
                _, file_extension = os.path.splitext(src_file)
                file_extension = file_extension.lower()
                destination = None

                if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                    destination = image_directory
                elif file_extension in ['.mp4', '.avi', '.mkv']:
                    destination = video_directory
                elif file_extension in ['.pdf', '.doc', '.docx', '.txt']:
                    destination = documents_directory
                elif file_extension in ['.mp3', '.wav']:
                    destination = audio_directory
                else:
                    destination = other_directory

                destination_file = os.path.join(destination, os.path.basename(src_file))
                shutil.move(src_file, destination_file)
                print(f"Moved {src_file} to {destination_file}")

    def on_created(self, event):
        if event.is_directory:
            return
        self.organize_existing_files()

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
