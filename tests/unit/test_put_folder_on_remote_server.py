import pysftp
import pytest
import paramiko
from actions import put_folder_on_remote_server as put_r


def test_no_folder(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    assert put_r.put_r(sftp, "totes.not.fake.no.really") is False
    assert put_r.ERROR_MESSAGE in capsys.readouterr().out

def test_best_case(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """
    assert put.put(sftp, "main.py") is True

