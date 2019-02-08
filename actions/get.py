#Close Connection
from app import login
from tests.test_server import HOSTNAME, USERNAME, PASSWORD
import os

# Close connection to a server
# TODO Do we want to preserve the time of the file creation on the server or do we want
#  or do we want create a new creation time?
def get(sftp, remotepath, localpath, preserve_mtime=True):
    """Processes the close connection request. Note that pysftp does not
       return any kind of error if the close is succesful.
       If a connection did not close, however, this code raises an exception
    """
    print(remotepath)
    print(localpath)
    return sftp.get(remotepath, os.curdir, callback=None, preserve_mtime=True)

'''
sftp = login.login(HOSTNAME,
                   USERNAME,
                   PASSWORD)
get(sftp, os.curdir)
'''