import pysftp

ERROR_MESSAGE = "Sorry, we couldn't find your folder locally. Please check your spelling and try again"


def put_r(sftp: pysftp.Connection, foldername: str):
    """ There is a lot wrong with the pysftp imlementation of put_r. It:
    1. Does not copy the directory on the remote machine, only its contents.
    2. Changes into the current local directory before copying contents
       using os.chdir(). This causes an exception to be thrown that the folder is not
       found (because current path is IN the directory)

    As a result, our code has to:
    1. Manually create a remote directory of the localpath's name we want to copy.
    2. Manually step into that remote directory (so no error is thrown).
       Then call pysftp's function to copy the local contents.

    Also note: put_r works, while put_d does not work. put_d has separate, but similar issues.
    makedirs is used instead of mkdirs, because makedirs will throw an
    exception if the directory already exists on the remote server. This is also why we
    have a try/except block.
    """

    try:
        # Make remote directory
        try:
            sftp.makedirs(foldername)
        except OSError:
            print("Sorry, folder already exists on remote.")
            return False
        # Change into current remote directory
        sftp.chdir(foldername)
        # Copy contents of local directory into remote directory
        sftp.put_r(foldername, ".", preserve_mtime=False)
        return True

    except OSError:
        # IF an error occurs at this line, the put_r failed, and we need to remove the previous directory.
        print(ERROR_MESSAGE)
        sftp.rmdir(foldername)
        return False
