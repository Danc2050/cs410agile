import pysftp

ERROR_MESSAGE = "Sorry, we couldn't find your folder locally. Please check your spelling and try again"


def put_r(sftp: pysftp.Connection, foldername: str):
    """ There is a lot wrong with the pysftp imlementation of put_r. It:
    1. Does not copy the directory on the remote machine, only its contents.
    2. Changes into a directory (which doesnt exist) using os.chdir() before copying contents.
       This causes an exception to be thrown that the folder is not found
       (because there is no directory)

    As a result, our code has to:
    1. manually create a remote directory of the localpath's name we want to copy.
    2. manually step into that remote directory (so no error is thrown).
    3. then call pysftp's put_r function to copy the local contents.
    
    ***Notes***:
        * if there is no such file on the local machine, we must remove the folder we created in the exception block.
        * put_r works, while put_d does not work. put_d has separate, but similar issues.
        * makedirs is used instead of mkdirs, because makedirs will throw an exception if the directory already
          exists on the remote server. This is also why we nest this in a try/except block.
    """

    try:
        # 1) make remote directory
        try:
            sftp.makedirs(foldername)
        except OSError:
            print("Sorry, folder already exists on remote.")
            return False
        # 2) change into current remote directory
        sftp.chdir(foldername)
        # 3) copy contents of local directory into remote directory
        sftp.put_r(foldername, ".", preserve_mtime=False)
    except FileNotFoundError as error:
        print(error)
        sftp.chdir("..")
        # remove folder created on remote if there is no such folder on local machine.
        sftp.rmdir(foldername)
        return False
    # if everything went fine, then the folder's contents have been copied. Return True.
    return True
