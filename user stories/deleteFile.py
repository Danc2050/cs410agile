#delete file from server
def delete(sftp):
    try:
        sftp.rmdir('put')
    except Exception as error:
        print("Remove file error message: " + str(error.args))
    else:
        print("Remove command succeeded")