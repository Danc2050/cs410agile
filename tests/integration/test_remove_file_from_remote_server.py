from actions import remove_from_remote_server
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_rm()
# and check for in our tests.
SUCCESS_STRING = "mock_rm CALLED"

# The fake filename to pass in.
FILENAME = "filename"


def mock_rm(sftp:pysftp.Connection, filename: str):
    """A fake remove_from_remote_server() function that checks the arguments and prints a string we
    can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    assert filename == FILENAME
    print(SUCCESS_STRING)


def test_remove_file_invokes_remove_function(capsys, monkeypatch, sftp):
    """Tests that writing 'rm file' calls the remove_from_remote_server action and passes 'file'
    as the filename.
    """

    # Replace remove_from_remote_server.remove_from_remote_server with our mocked function
    monkeypatch.setattr(remove_from_remote_server, "remove_from_remote_server", mock_rm)

    # Pass in a valid input
    with mock_input("rm " + FILENAME):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_rm_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the rm action."""

    # See tests/integration/test_close.py for details.
    with mock_input("putty"):
        main_loop(sftp)
        assert "not recognized" in capsys.readouterr().out
