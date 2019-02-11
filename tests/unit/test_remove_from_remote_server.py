
from actions import remove_from_remote_server as rm

REAL_FILE = "unicorns.py"
FAKE_FILE = "sadnessForever.txt"

def remove_item_that_exists(sftp):
    # TODO add something which automatically adds a file, so we can test deleting a file that is real
    assert rm.remove_from_remote_server(REAL_FILE) is True


def remove_item_that_does_not_exist(sftp):
    assert rm.remove_from_remote_server(FAKE_FILE) is False
    assert rm.ERROR_MESSAGE
