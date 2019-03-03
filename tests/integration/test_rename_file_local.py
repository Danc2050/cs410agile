from actions import rename_files_local
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_rename CALLED"

# The fake filename to pass in.
FROM = "fromfile"
TO = "tofile"


def mock_rename(before: str, after: str):
    """A fake rename_local_file() function that checks the arguments and prints 
    a string we can check for, to verify that the function was called.
    """

    assert before == FROM
    assert after == TO
    print(SUCCESS_STRING)


def test_lrename_invokes_rename_action(capsys, monkeypatch, sftp):
    """Tests that writing text like 'lrename from to' calls the put action and
    passes 'from' as the original filename and 'to' as the new filename.
    """

    # Replace the real action with our mocked function
    monkeypatch.setattr(rename_files_local, "rename_local_file", mock_rename)

    # Pass in a valid input
    with mock_input("lrename {} {}".format(FROM, TO)):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_rename_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the rename action."""

    # See tests/integration/test_close.py for details.
    test_inputs = [
        "doesnotexist",
        "lrename",  # No files
        "lrename onefile",
        "lrename onefile twofile threefile"
    ]
    for test in test_inputs:
        with mock_input(test):
            main_loop(sftp)
            assert "not recognized" in capsys.readouterr().out

