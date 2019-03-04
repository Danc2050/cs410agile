import pysftp

ERROR_PREFIX = "Error:"
ERROR_MESSAGE = "Unable to change permissions."

def change_permissions(sftp, permission, filename):
    try:
        sftp.chmod(filename, permission)
        return True

    except OSError as e:
        if e.strerror is None:
            print(ERROR_PREFIX, ERROR_MESSAGE)
        else:
            print(ERROR_PREFIX, e.strerror)
        return False
