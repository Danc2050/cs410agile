from actions import change_permissions_remote as chmod
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_chmod CALLED"

# The parameters to pass in
MODE = '777'
PATH = "test_path"


def mock_chmod(sftp: pysftp.Connection, permissions: int, path: str):
    """A fake change_permissions() function that checks the arguments and prints
    a string we can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    assert permissions == MODE
    assert path == PATH
    print(SUCCESS_STRING)


def test_chmod_invokes_chmod_action(capsys, monkeypatch, sftp):
    """Tests that writing text like 'chmod 555 mydir' calls the rename action
    and passes 777 and 'mydir' as permissions and filename, respectively.
    """

    # Replace the real action with our mocked function
    monkeypatch.setattr(chmod, "change_permissions", mock_chmod)

    # Pass in a valid input
    with mock_input("chmod {} {}".format(MODE, PATH)):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_chmod_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the chmod action."""

    # Test inputs. They need to be a single sequence, or we'll send EOF
    # and close our SFTP connection after the first test.
    test_inputs = """
                  doesnotexist
                  chmod
                  chmod 777
                  chmod 777 fileone filetwo
                  """
    for test in test_inputs:
        with mock_input(test):
            main_loop(sftp)
            assert SUCCESS_STRING not in capsys.readouterr().out
