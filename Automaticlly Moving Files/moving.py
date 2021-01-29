from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog

import os
import json
import time


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):

        for filename in os.listdir(folder_to_track):

            src = folder_to_track + "/" + filename

            old_file_name = os.path.basename(src)

            new_name = date + "__" + old_file_name

            # file_exists = os.path.isfile(folder_destination + "/" + new_name)

            new_destination = folder_destination + "/" + new_name

            os.rename(src, new_destination)


folder_to_track = "/Users/teun/OneDrive/Bureaublad/testFolder1"
folder_destination = "/Users/teun/OneDrive/Bureaublad/testFolder2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
        date = time.strftime('%Y-%m-%d-%S', time.localtime())
        print("Try on: " + date)
except KeyboardInterrupt:
    observer.stop()
observer.join()
