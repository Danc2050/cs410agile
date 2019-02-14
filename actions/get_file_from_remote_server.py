import os

# This gets a file from a remote server.

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


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
    except FileNotFoundError:
        if not local_file_exists:  # Check to see if the file already exists locally or not
            os.remove(remote_file_name)  # Required because it will create the file locally if not found remotely
        print(ERROR_MESSAGE)
        return False
