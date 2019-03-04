import os

# This gets a file from a remote server.

FILE_NOT_FOUND_ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"
PERMISSION_ERROR_MESSAGE = "Sorry, you do not have permissions"
IS_DIRECTORY_ERROR = "Sorry, but that file already exists as a directory"
IO_ERROR_MESSAGE = "Sorry, there was an IO error"


def get(sftp, remote_file_name):
    """Gets multiple files from a remote server in series
    """
    local_file_path = os.curdir + '/' + remote_file_name

    # Check if file exists locally first
    if os.path.isfile(local_file_path):
        local_file_exists = True
    else:
        local_file_exists = False

    try:
        sftp.get(remote_file_name, local_file_path, callback=None)
        return True
    except IOError:
        print(IO_ERROR_MESSAGE)
        return False
    except FileNotFoundError:
        if not local_file_exists:  # Check to see if the file already exists locally or not
            os.remove(remote_file_name)  # Required because it will create the file locally if not found remotely
        print(FILE_NOT_FOUND_ERROR_MESSAGE)
        return False
    except PermissionError:
        print(PERMISSION_ERROR_MESSAGE)
        return False
    except IsADirectoryError:
        print(IS_DIRECTORY_ERROR)
        return False
