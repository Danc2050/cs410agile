from actions import rename_file_remote as rename
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_rename CALLED"

# The fake filename to pass in.
FROM = "from_test_file"
TO = "to_test_file"


def mock_rename(sftp: pysftp.Connection, before: str, after: str):
    """A fake rename_remote_file() function that checks the arguments and prints
    a string we can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    assert before == FROM
    assert after == TO
    print(SUCCESS_STRING)


def test_rename_invokes_rename_action(capsys, monkeypatch, sftp):
    """Tests that writing text like 'rename from to' calls the rename action
    and passes 'from' and 'to' as before and after, respectively.
    """

    # Replace the real action with our mocked function
    monkeypatch.setattr(rename, "rename_remote_file", mock_rename)

    # Pass in a valid input
    with mock_input("rename {} {}".format(FROM, TO)):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_mkdir_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the rename action."""

    # Test inputs. They need to be a single sequence, or we'll send EOF
    # and close our SFTP connection after the first test.
    test_inputs = """
                  doesnotexist
                  rename
                  rename one
                  rename one two three
                  """
    for test in test_inputs:
        with mock_input(test):
            main_loop(sftp)
            assert SUCCESS_STRING not in capsys.readouterr().out
