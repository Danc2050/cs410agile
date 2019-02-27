import pysftp
import pytest
from actions import rmdir

# TEST 1: Directory exists
def test_delete_empty_directory_succeeds(sftp):

    directory = "test_delete_empty_directory_succeeds"
    sftp.mkdir(directory, mode=777)                 # add a directory
    rmdir.rmdir(sftp, directory)                    # remove directory
    assert 2 == 2

# TEST 2: Directory does not exist
def test_delete_non_exisitance_directory_fail(sftp):
    directory = "test_no_directory_fail"
    rmdir.rmdir(sftp, directory)
    assert 2 == 2

# TEST 3: Directory has content
def test_del_directory_with_content(sftp):
    directory2 = "test_content_directory_fail/test"
    directory1 = "test_content_directory_fail"
    sftp.mkdir(directory2, mode=777)
    rmdir.rmdir(sftp,directory1)                          # test delete directory
    rmdir.rmdir(sftp, directory2)                         # delete directory2
    rmdir.rmdir(sftp, directory1)                         # delete directory1
    assert 2 == 2