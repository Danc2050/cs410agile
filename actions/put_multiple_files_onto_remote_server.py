import pysftp
import actions.put_file_onto_remote_server as put

# This puts multiple files onto the server. It attempts to put each valid file found
# onto the server and gives an error message for each file not found. If more than
# 0 files are added it is considered a success.

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


def put_multiple(sftp: pysftp.Connection, filenames: [], num_files: int):
    success = False

    for i in range(0, num_files):
        ret = put.put(sftp, filenames[i])
        if not ret:
            print("filename in question:" + filenames[i])
            print()
            continue
        else:
            success = True

    return success

