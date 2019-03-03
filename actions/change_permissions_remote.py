import pysftp


ERROR_MESSAGE = "Can not change permissions. No such file exists"


def change_permissions(sftp, permission, filename):
    try:
        sftp.chmod(filename, permission)
        return True

    except IOError:
        print(ERROR_MESSAGE)
        return False
