#get file from server  --- NOTE: I COULD NOT GET THIS TO WORK. IT DOES NOT CURRENTLY WORK
def get(sftp, path):
    try:
        sftp.get(remotepath=path, localpath='~/PycharmProjects/SFTP', preserve_mtime=True) #last arg preserves file metadata
    except Exception as error:
        print("Get error message " + str(error.args))
    else:
        print("Get command succeeded")