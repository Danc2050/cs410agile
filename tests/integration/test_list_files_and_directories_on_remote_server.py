from actions import listdir
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_remote_listdir CALLED"

# The fake filename to pass in.
FILENAME = "filename"


def mock_list_dir(sftp:pysftp.Connection):
    """A fake list_dir() function that checks the arguments and prints a string
    we can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    print(SUCCESS_STRING)


def test_put_file_invokes_put_function(monkeypatch, capsys, sftp):
    """Tests that writing 'put file' calls the put action and passes 'file'
    as the filename.
    """

    # Replace the action with our mocked function
    monkeypatch.setattr(listdir, "list_dir", mock_list_dir)

    # Pass in a valid input
    with mock_input("ls"):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_put_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the put action."""

    # See tests/integration/test_close.py for details.
    test_input = """
                 definitely_not_a_command
                 ls mydir
                 """
    with mock_input(test_input):
        main_loop(sftp)
        assert SUCCESS_STRING not in capsys.readouterr().out
