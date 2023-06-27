# 2. Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []

    for entry in os.scandir(path):
        if entry.is_dir():
            directories.append(entry.name)
            all_directories_files.append(entry.name)
        elif entry.is_file():
            files.append(entry.name)
            all_directories_files.append(entry.name)

    print("Directories:")
    print(directories)
    print("\nFiles:")
    print(files)
    print("\nAll Directories/Files:")
    print(all_directories_files)

# Specify the path you want to list
path = '/path/to/directory'

list_directories_files(path)
