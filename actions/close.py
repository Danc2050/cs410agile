#Close Connection
import pysftp
from app import login

# Close connection to a server
def close(sftp):
    """Processes the close connection request. Note that pysftp does not
       return any kind of error if the close is succesful.
       If a connection did not close, however, this code raises an exception
    """
    return sftp.close()
