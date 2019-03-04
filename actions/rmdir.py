#Remove Directory

usage = "Error: no such file or directory contains content at "

# Remove directory on server
def rmdir(sftp, directory):
    """Removes a directory either with the file path or the name of the directory
    """
    try:
        sftp.rmdir(directory)
        return True
    except OSError as e:
        if e.strerror is None:
            print("Could not remove directory.")
        else:
            print("Error:", e.strerror)
        return False

# end
