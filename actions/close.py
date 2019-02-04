#Close Connection
import pysftp

# Close connection to a server
def close(sftp):
    """Processes the close connection request. Note that pysftp does not
       return any kind of error if the close is succesful.
       If a connection did not close, however, this code raises a "home made"
       exception
    """
    return sftp.close()
