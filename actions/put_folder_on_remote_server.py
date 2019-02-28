import pysftp

ERROR_MESSAGE = "Sorry, we couldn't find your folder locally. Please check your spelling and try again"
PERMISSION_ERROR = "You do not have the proper permissions for this directory."

def put_r(sftp: pysftp.Connection, foldername: str):
    """ There is a lot wrong with the pysftp imlementation of put_r. It:
    1. does not check if a folder exists already.
    2. does not copy the directory on the local machine, only its contents.
    3. changes into a directory (which doesnt exist) using os.chdir() before copying contents.
       This causes an exception to be thrown that the folder is not found
       (because there is no directory)

    As a result, our code has to:
    1. manually check if a folder exists already.
    2. create a remote directory of the local folder name we want to copy if it does not exist.
    3. manually step into that remote directory (so no error is thrown).
    4. then call pysftp's put_r function to copy the local contents.
    5. finally, step out of the remote directory.

    ***Notes***:
        * if there is no such file on the local machine, we must remove the folder we created in the exception block.
        * put_r works, while put_d does not work. put_d has separate, but similar issues.
    """

    try:
        # 1) Change into the remote directory, if it exists.
        try:
            sftp.chdir(foldername)
        except:
            # 2) make remote directory, if it does not exist.
            sftp.makedirs(foldername)
            # 3) change into current remote directory
            sftp.chdir(foldername)
        # 4) copy contents of local directory into remote directory
        sftp.put_r(foldername, ".", preserve_mtime=False)

        # 5) change out of the remote directory.
        sftp.chdir("..")
    except FileNotFoundError as error:
        sftp.chdir("..")
        # remove folder created on remote if there is no such folder on local machine.
        sftp.rmdir(foldername)
        print(ERROR_MESSAGE)
        return False
    except PermissionError:
        print(PERMISSION_ERROR)
        return False
    # if everything went fine, then the folder's contents have been copied. Return True.
    return True
