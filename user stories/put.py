#Put file on server
def put(sftp, file): #file = '~/PycharmProjects/SFTP/user stories/put' in sample case.
    try:
        sftp.put(file, preserve_mtime=True)
    except Exception as error:
        print("Put error message: " + str(error.args))
    else:
        print("put command succeeded")