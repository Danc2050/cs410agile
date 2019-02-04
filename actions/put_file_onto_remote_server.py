import pysftp as sftp

# this puts a file onto a remote server, The preserve mtime = true
# will make sure that the modification times on the server copy match those
# on the local machine


def put(filename):
    return sftp.put(filename, preserve_mtime=True)
