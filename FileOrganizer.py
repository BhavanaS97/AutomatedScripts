import os
import shutil
import stat

# Define source path
src_dir = "/Users/vinaykumarvommi/Desktop/Automation" #Path
file_categories = {
    "Images": ['jpg', 'jpeg', 'png', 'gif'],
    "Documents": ['pdf', 'docx', 'txt'],
    "Audio": ['mp3', 'wav'],
}

# Check read and write permissions
if os.access(src_dir, os.R_OK) and os.access(src_dir, os.W_OK):
    print("You have permissions")
else:
    try:
        # Change permissions to read and write for the user
        os.chmod(src_dir, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)  # Adding execute permission for directories
        if os.access(src_dir, os.W_OK):
            print("Permissions changed successfully. You now have write access.")
        else:
            print("Failed to change permissions for write access.")
    except Exception as e:
        print(f"Error changing permissions: {e}")

# Organize files into folders
for file in os.listdir(src_dir):
    # Get the file extension safely
    #print(file)
    file_ext = file.split('.')[-1] if '.' in file else None
    #print(file_ext)
    # Check if file_ext is not None and categorize
    if file_ext:
        for category, extensions in file_categories.items():
            if file_ext.lower() in extensions:  # Use lower() to avoid case sensitivity
                category_dir = os.path.join(src_dir, category)
                os.makedirs(category_dir, exist_ok=True)  # Create category directory if it doesn't exist
                # Move the file to the corresponding category folder
                shutil.move(os.path.join(src_dir, file), os.path.join(category_dir, file)) #os.path.join(category_dir, file): This constructs the target path where the file will be moved. The category_dir is the destination directory, and file is the name of the file being moved.
                print(f"Moved file: {file} to {category_dir}")
                break
    else:
        print(f"File {file} has no extension and will be skipped.")