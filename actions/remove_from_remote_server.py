import pysftp

ERROR_MESSAGE = "The file/folder you tried to delete did not exist. Please check your spelling and try again"


def remove_from_remote_server(sftp, filename):
    try:
        sftp.remove(filename)
        return True
    except IOError:
        print(ERROR_MESSAGE)
        return False

