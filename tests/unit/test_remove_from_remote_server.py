from actions import remove_from_remote_server as rm
from actions import put_file_onto_remote_server as put

REAL_FILE = "main.py"
FAKE_FILE = "sadnessForever.txt"


def remove_item_that_exists(sftp):
    put(sftp, REAL_FILE)
    assert rm.remove_from_remote_server(REAL_FILE) is True


def remove_item_that_does_not_exist(sftp, capsys):
    assert rm.remove_from_remote_server(FAKE_FILE) is False
    assert put.ERROR_MESSAGE in capsys.readouterr().out

