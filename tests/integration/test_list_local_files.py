from actions import list_files_local
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_list_local_files CALLED"


def mock_list_local_files():
    """A fake display_local_files() function that prints a string we
    can check for, to verify that the function was called.
    """

    print(SUCCESS_STRING)


def test_lls_invokes_list_files_local_action(capsys, monkeypatch, sftp):
    """Tests that writing 'lls' calls the 'list files local' action."""

    # Replace the real function with our mocked function
    monkeypatch.setattr(list_files_local,
                        "display_local_files",
                        mock_list_local_files)

    # Pass in a valid input
    with mock_input("lls"):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_list_local_files_action(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the 'list local
    files action.
    """

    # See tests/integration/test_close.py for details.
    with mock_input("putty"):
        main_loop(sftp)
        assert "not recognized" in capsys.readouterr().out
