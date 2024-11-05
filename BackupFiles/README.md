# File Backup Script

This Python script is designed to create a backup of files from a specified source directory to a designated destination directory. The backup is stored in a new folder that includes a timestamp to ensure uniqueness.

## Features

- Recursively copies all files and subdirectories from the source directory to the backup directory.
- Creates a new backup folder with a timestamp to avoid overwriting previous backups.
- Uses the `shutil` library to handle file operations efficiently.

## Requirements

- Python 3.x
- `shutil` module (included in the Python Standard Library)
- `os` module (included in the Python Standard Library)
- `datetime` module (included in the Python Standard Library)

## Usage

1. **Set the Source and Destination:**
   Update the `backup_files` function call at the end of the script with the desired source and destination paths.

   ```python
   backup_files('/path/to/source', '/path/to/destination')

