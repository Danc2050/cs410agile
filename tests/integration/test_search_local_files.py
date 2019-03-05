from actions import search_local_files as lsearch
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_lsearch CALLED"

# The fake filename to pass in.
NAME = "my_search_pattern"


def mock_lsearch(name: str):
    """A fake lsearch() function that checks the arguments and prints
    a string we can check for, to verify that the function was called.
    """

    assert name == NAME
    print(SUCCESS_STRING)


def test_lsearch_invokes_lsearch_action(capsys, monkeypatch, sftp):
    """Tests that writing text like 'lsearch myname' calls the lsearch action and
    passes 'myname' as name.
    """

    # Replace the real action with our mocked function
    monkeypatch.setattr(lsearch, "search_local_files", mock_lsearch)

    # Pass in a valid input
    with mock_input("lsearch {}".format(NAME)):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_lsearch_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the lsearch action."""

    # See tests/integration/test_close.py for details.
    test_inputs = [
        "doesnotexist",
        "lsearch",  # No files
        "lsearch onefile twofile"
    ]
    for test in test_inputs:
        with mock_input(test):
            main_loop(sftp)
            assert SUCCESS_STRING not in capsys.readouterr().out


