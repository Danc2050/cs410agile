import pysftp
from tests import test_server

#Connect to Server
def login(host, username, password):
    try:
        sftp = pysftp.Connection(host =host, username=test_server.USERNAME, password=test_server.PASSWORD)
    except Exception as error:
        print("Connection error message: " + str(error.args))
        return error
    else:
        print("Authentication success.")
    return sftp