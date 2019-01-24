#list files/folders on server
def ls(sftp, remotepath): #remotepath = '/u/danc2' (a string) as an example.
    try:
        list = sftp.listdir(remotepath=remotepath)
    except Exception as error:
        print("LS failed: " + str(error.args))
    else:
        print(list)