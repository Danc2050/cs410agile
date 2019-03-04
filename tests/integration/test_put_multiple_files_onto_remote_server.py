from actions import put_multiple_files_onto_remote_server as mput
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_mput CALLED"

# The fake filename to pass in.
FILENAMES = "file1 file2 file3"
FILENAME_LIST = ["file1", "file2", "file3"]


def mock_mput(sftp:pysftp.Connection, filenames: [str]):
    """A fake put_multiple() function that checks the arguments and prints a
    string we can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    assert filenames == FILENAME_LIST
    print(SUCCESS_STRING)


def test_put_file_invokes_put_function(capsys, monkeypatch, sftp):
    """Tests that writing 'mput file1 file1' calls the mput action and passes
    the list ["file1", "file2"] as filenames.
    """

    # Replace put_file_onto_remote_server.put with our mocked function
    monkeypatch.setattr(mput, "put_multiple", mock_mput)

    # Pass in a valid input
    with mock_input("mput " + FILENAMES):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_mput_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the mput action."""

    inputs = """
             cluckcluckcluck
             mput
             """
    with mock_input(inputs):
        main_loop(sftp)
        assert SUCCESS_STRING not in capsys.readouterr().out
