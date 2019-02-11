import pysftp

# this puts a file onto a remote server, The preserve mtime = true
# will make sure that the modification times on the server copy match those
# on the local machine


def put(sftp: pysftp.Connection, filename: str):
    try:
        sftp.put(filename, filename, preserve_mtime=False)

    except FileNotFoundError:
        print("Sorry, we couldn't find your file. Please check your spelling and try again")

