#Close Connection
def close(sftp):
    try:
        sftp.close()
    except Exception as error:
        print("Close connection error message: " + str(error.args))
    else:
        print("SFTP Close Suceeded.")