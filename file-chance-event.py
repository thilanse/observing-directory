import os
import shutil
import re
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    def on_modified(self, event):
        print(event.src_path)
        for file in os.listdir(path):
            src_file = path + '/' + file
            dest_file = dest + '/' + file
            os.rename(src_file, dest_file)


path = "F:/Projects/python-scripts/data"
dest = "F:/Projects/python-scripts/dest"
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
