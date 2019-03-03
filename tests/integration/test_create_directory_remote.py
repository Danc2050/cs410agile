from actions import create_directory_on_remote as mkdir
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_mkdir CALLED"

# The fake filename to pass in.
FOLDER = "testfolder"


def mock_mkdir(sftp: pysftp.Connection, path: str):
    """A fake create_dir_remote() function that checks the arguments and prints
    a string we can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    assert path == FOLDER
    print(SUCCESS_STRING)


def test_mkdir_invokes_create_folder_action(capsys, monkeypatch, sftp):
    """Tests that writing text like 'mkdir foldername' calls the put action and
    passes 'foldername' as the remote path to create.
    """

    # Replace the real action with our mocked function
    monkeypatch.setattr(mkdir, "create_dir_remote", mock_mkdir)

    # Pass in a valid input
    with mock_input("mkdir {}".format(FOLDER)):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_mkdir_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the mkdir action."""

    # Test inputs. They need to be a single sequence, or we'll send EOF
    # and close our SFTP connection after the first test.
    test_inputs = """
                  doesnotexist
                  mkdir
                  mkdir thing1 thing2
                  """
    for test in test_inputs:
        with mock_input(test):
            main_loop(sftp)
            assert SUCCESS_STRING not in capsys.readouterr().out
