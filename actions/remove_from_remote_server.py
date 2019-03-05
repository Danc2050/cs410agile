import pysftp

ERROR_PREFIX = "Error:"
ERROR_MESSAGE = "We couldn't delete your file. Sorry :( "


def remove_from_remote_server(sftp, filename):
    try:
        sftp.remove(filename)
        return True
    except OSError as e:
        if e.strerror is None:
            print(ERROR_PREFIX, ERROR_MESSAGE)
        else:
            print(ERROR_PREFIX, e.strerror)
        return False

