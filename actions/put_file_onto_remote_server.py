import pysftp

# this puts a file onto a remote server, The preserve mtime = true
# will make sure that the modification times on the server copy match those
# on the local machine

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"

def put(sftp: pysftp.Connection, filename: str):
    try:
        sftp.put(filename, filename, preserve_mtime=False)
        return True

    except FileNotFoundError:
        print(ERROR_MESSAGE)
        return False

