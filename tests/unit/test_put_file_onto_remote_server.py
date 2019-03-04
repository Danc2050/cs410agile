import pysftp
import pytest
import paramiko
import os
from actions import put_file_onto_remote_server as put


def test_no_file(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """
    assert put.put(sftp, "totes.not.fake.no.really") is False
    assert put.ERROR_MESSAGE in capsys.readouterr().out

def test_put_file_with_absolute_path(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """
    test_dir="folder1/folder2"
    file_test = "file_test.txt"
    os.makedirs(test_dir)
    open(test_dir + '/' + file_test, 'a').close()

    assert put.put(sftp, test_dir + '/' + file_test) is True
    assert sftp.isfile(file_test) is True

    sftp.remove(file_test) 

    os.remove(test_dir + '/' + file_test)
    os.removedirs(test_dir)



def test_best_case(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """
    assert put.put(sftp, "main.py") is True

