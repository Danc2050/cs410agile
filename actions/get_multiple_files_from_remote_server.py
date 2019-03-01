import pysftp
import actions.get_file_from_remote_server as get

# This gets multiple files from the remote server.

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


def get_multiple(sftp: pysftp.Connection, filenames: [], num_files: int):
    success = False

    for i in range(0, num_files):
        ret = get.get(sftp, filenames[i])
        if not ret:
            print("filename in question:" + filenames[i])
        else:
            success = True

    return success
