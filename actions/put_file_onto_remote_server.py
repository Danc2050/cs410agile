import pysftp

# this puts a file onto a remote server, The preserve mtime = true
# will make sure that the modification times on the server copy match those
# on the local machine


def put(sftp: pysftp.Connection, filename: str):
    return sftp.put(filename, preserve_mtime=True)
