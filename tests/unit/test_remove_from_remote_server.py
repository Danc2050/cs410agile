from actions import remove_from_remote_server as rm
from actions import put_file_onto_remote_server as put
import pysftp

REAL_FILE = "main.py"
FAKE_FILE = "sadnessForever.txt"


def remove_item_that_exists(sftp):
    put(sftp, REAL_FILE)
    assert rm.remove_from_remote_server(REAL_FILE) is True


def remove_item_that_does_not_exist(sftp, capsys):
    """
    this asks to remove a thing which isn't a file, and
    confirms the function doesn't remove it
    """
    assert rm.remove_from_remote_server(FAKE_FILE) is False
    assert put.ERROR_MESSAGE in capsys.readouterr().out


def check_if_deletes_directory(sftp):
    """ This test makes a directory, tests that that remove file
    of the same name doesn't remove the directory, then removes
    the directory
    """
    sftp.makedirs(REAL_FILE)
    assert rm.remove_from_remote_server(REAL_FILE) is False
    sftp.rmdir(REAL_FILE)

