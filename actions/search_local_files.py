# Search local Directory and subdirectories
import os


def search_local_files(name):
    rootdir = os.getcwd()
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        filepath = subdir + os.sep
        for dir in dirs:
            if name in dir:
                # Directory match! Print the relative path.
                print(os.path.relpath(filepath + dir))
                count = count + 1
        for file in files:
            filepath = subdir + os.sep + file
            if name in file:
                # File match! Print the relative path.
                print(os.path.relpath(filepath))
                count = count + 1
    if count < 1:
        print("File not found")
    return count
