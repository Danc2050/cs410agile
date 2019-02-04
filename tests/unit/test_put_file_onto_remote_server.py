import pysftp
import pytest
import paramiko
from actions import put_file_onto_remote_server as put


def test_no_file(sftp):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """
    with pytest.raises(OSError):
        put.put(sftp, "snuggleSauce.txt")




#def test_bad_path():
    """Test what happens when you give it a bad path.
    """
    #return 0


#def test_best_case():
    """Count the number of files on disk and
    remote server before the put operation

    Preform operation

    count after and insure that there is one less file
    locally and one more on the server
    """

 #   return 0
