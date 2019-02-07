#Remove Directory
import pysftp

# Remove directory on server
def rmdir(sftp, directory):
    """Remove directory in current working directory
    """
    sftp.rmdir(directory)