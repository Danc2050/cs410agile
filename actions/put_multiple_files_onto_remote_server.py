import pysftp
import actions.put_file_onto_remote_server as put

# This puts multiple files onto the server. It attempts to put each valid file found
# onto the server and gives an error message for each file not found. If more than
# 0 files are added it is considered a success.

ERROR_MESSAGE = "Sorry, we couldn't find your file. Please check your spelling and try again"


def put_multiple(sftp: pysftp.Connection, filenames: []):
    success = False

    for filename in filenames:
        # Print a header, without the newline
        print("Putting " + filename + ": ", end="")
        try:
            if put.put(sftp, filename):
                print("OK")
                success = True
            # Else, put() printed an error message.
        except OSError as e:
            if e.strerror is None:
                print("Couldn't put file.")
            else:
                print(e.strerror)

    return success

