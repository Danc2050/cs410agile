import pysftp

# List directory on remote machine


def list_dir(sftp: pysftp.Connection):
    """sftp.listdir() returns a list containing the names of files in the current (".") directory.
    Note: It does not print the list, so we must return the list to main for that to be done.
    """
    return sftp.listdir(".")
