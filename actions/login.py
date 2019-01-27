import pysftp
from tests import test_server

#Connect to Server
def login(HOST, USERNAME, PASSWORD):
    try:
        sftp = pysftp.Connection(host=HOST, username=USERNAME, password=PASSWORD)
    except Exception as error:
        print("Connection error message: " + str(error.args))
        return error
    else:
        print("Authentication success.")
    return sftp