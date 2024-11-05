import os
import shutil
from datetime import datetime

def backup_files(source, destination):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S") #convert datetime object into string based on format
    dest_folder = os.path.join(destination, f"backup_{timestamp}")
    os.makedirs(dest_folder, exist_ok=True)
    print(f"Backup folder created: {dest_folder}")
    shutil.copytree(source, dest_folder,dirs_exist_ok=True) #The shutil.copytree() function in Python is used to recursively copy an entire directory tree from a source directory to a destination directory. This means it copies all the files and subdirectories from the source to the destination, preserving the directory structure.
    #You don’t need to explicitly write a loop to go through the files because copytree() automatically handles that for you
# Usage
backup_files('/Users/vinaykumarvommi/Desktop/Automation' , '/Users/vinaykumarvommi/Desktop/BackupFiles')