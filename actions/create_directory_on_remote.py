import pysftp


ERROR_PREFACE = "Error:" 

def create_dir_remote(sftp: pysftp.Connection, remotepath: str):
    try:
        sftp.mkdir(remotepath, mode=777)
        return True

    except OSError as e:
        print(ERROR_PREFACE, e.strerror)
        return False
