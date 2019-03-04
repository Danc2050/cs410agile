# Search local Directory and subdirectories
import os

def searchLocal(name):
    rootdir = os.getcwd()
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        filepath = subdir + os.sep
        for dir in dirs:
            if dir.endswith(name):
                print(filepath + dir)
                count = count + 1
        for file in files:
            filepath = subdir + os.sep + file
            if file.startswith(name):
                print(filepath)
                count = count + 1
    if count < 1:
        print("File not found")
    return count