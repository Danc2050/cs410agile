# Search local Directory and subdirectories
import os

def searchLocal(name):
    rootdir = os.getcwd()
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file
            if file.startswith(name):
                print(filepath)
                count = count + 1
    return count