import pysftp
import actions.get_file_from_remote_server as get

# This gets multiple files from the remote server.

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


def get_multiple(sftp: pysftp.Connection, filenames: []):
    success = False

    for filename in filenames:
        # Print a header, without the newline
        print("Getting " + filename + ": ", end="")
        try:
            if get.get(sftp, filename):
                print("OK")
                success = True
            # Else, get() printed an error message.
        except OSError as e:
            if e.strerror is None:
                print("Couldn't put file.")
            else:
                print(e.strerror)

    return success
