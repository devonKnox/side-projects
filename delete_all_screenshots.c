import os;
import shutil;

def delete_files_except_subfolder(directory, subfolder_name):
    for root, dirs, files in os.walk(directory):
        if os.path.basename(root) != subfolder_name:
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

# Example usage:
directory_path = r'C:\Users\11dkn\Desktop\Screenshots'
subfolder_name = 'For Fun'

delete_files_except_subfolder(directory_path, subfolder_name)
