import pysftp

# This puts a file onto a remote server, the preserve mtime = true
# will make sure that the modification times on the server copy match those
# on the local machine.

FOLDER_CONFLICT_ERROR_MESSAGE = "A folder by that name already exists."
FILE_NOT_FOUND_ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


def put(sftp: pysftp.Connection, filename: str):
    try:
        sftp.put(filename, filename, preserve_mtime=False)
        return True
    except FileNotFoundError:
        print("Error:", FILE_NOT_FOUND_ERROR_MESSAGE)
        return False
    except OSError:
        if sftp.isdir(filename):
            # The file  we want to upload is a directory on remote.
            # pysftp doesn't handle this case well, so we'll print a helpful
            # error message of our own.
            print("Error:", FOLDER_CONFLICT_ERROR_MESSAGE)
            return False
        else:
            # It's some other error; we'll let the main handler deal with it.
            raise
