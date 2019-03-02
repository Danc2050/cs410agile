from actions import change_permissions_remote as change
from actions import put_file_onto_remote_server as put

# Permissions that need changes
APPROVE = 0x0111
REAL_FILE = "main.py"


def test_no_file(sftp, capsys):
    """Test what happens when you ask to change the permissions on a
    file which doesn't exist.
    """
    assert change.change_permissions(sftp, "totes.not.fake.no.really", APPROVE) is False
    assert change.ERROR_MESSAGE in capsys.readouterr().out


def test_restrictive_permissions_case(sftp):
    """This tests if you try to change permissions on something you shouldn't
    have access to
    """
    assert change.change_permissions(sftp, "/home", APPROVE) is False
    # try to modify and verify it won't do anything


def test_allowing_permissions_case(sftp):
    sftp.put(sftp, REAL_FILE)
    assert change.change_permissions(sftp, REAL_FILE, APPROVE) is True
    # try to modify and verify it will do something!
    sftp.remove(sftp, REAL_FILE)
