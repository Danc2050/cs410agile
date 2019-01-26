from app.controller import main_loop
from app.input_handler import DEFAULT_USER_PROMPT
from tests.test_helpers import mock_input


def test_main_loop_disconnection(sftp):
    """Tests that the app handles disconnects gracefully."""

    # In order to test unexpected disconnects, we'll pass the controller
    # a disconnected sftp object and send a request take some basic action
    # that uses it.

    sftp.close()
    with mock_input("ls"):
        assert main_loop(sftp) == -1


def test_end_of_file(sftp, capsys):
    """Tests that the app handles the EOF character (e.g. Ctrl-D)
    gracefully.
    """

    with mock_input(""):
        retval = main_loop(sftp)
        stdout = capsys.readouterr().out
        assert retval == 0, \
            "Controller should return 0 after receiving EOF."
        assert ("connection closed" in stdout.lower()), \
            "EOF response message should include 'connection closed'."
        assert stdout.startswith("\n", len(DEFAULT_USER_PROMPT)), \
            "EOF response message should start with a newline."
