import pysftp
import actions.get_file_from_remote_server as get

# This gets multiple files from the remote server.

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


def get_multiple(sftp: pysftp.Connection, filenames: []):
    success = False

    for filename in filenames:
        ret = get.get(sftp, filename)
        if not ret:
            print("filename in question:" + filename)
        else:
            success = True

    return success
