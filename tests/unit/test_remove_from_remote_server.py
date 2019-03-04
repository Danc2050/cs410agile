from actions import remove_from_remote_server as rm
from actions import put_file_onto_remote_server as put
import pysftp

TEST_FILE_ONE = "test.txt"
TEST_FILE_TWO = "test2.txt"
FAKE_FILE = "sadnessForever.txt"


def test_remove_item_that_exists(sftp):
    sftp.open(TEST_FILE_ONE, "a").close()
    put(sftp, TEST_FILE_ONE)
    assert rm.remove_from_remote_server(sftp, TEST_FILE_ONE) is True


def test_remove_item_that_does_not_exist(sftp, capsys):
    """
    this asks to remove a thing which isn't a file, and
    confirms the function doesn't remove it
    """
    assert rm.remove_from_remote_server(sftp, FAKE_FILE) is False
    assert put.ERROR_MESSAGE in capsys.readouterr().out


def test_check_if_deletes_directory(sftp):
    """ This test makes a directory, tests that that remove file
    of the same name doesn't remove the directory, then removes
    the directory
    """
    sftp.makedirs(TEST_FILE_TWO)
    assert rm.remove_from_remote_server(sftp, TEST_FILE_TWO) is False
    sftp.rmdir(TEST_FILE_TWO)

