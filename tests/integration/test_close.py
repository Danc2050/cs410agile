from actions import close
from app.controller import main_loop
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_close()
# so we can check for it later.
SUCCESS_STRING = "mock_close CALLED"

# List of user inputs that should cause the close action to be invoked.
INPUTS = ["bye", "exit", "quit"]


def mock_close(sftp: pysftp.Connection):
    """A fake close() function that checks the argument type
    and prints a string we can check for, to verify that the
    function was called."""

    assert isinstance(sftp, pysftp.Connection)
    print(SUCCESS_STRING)

    # Note to other developers: printing a string and checking for it
    # is a really awkward way to test that the function was called,
    # but after 15 minutes or so of searching online, I didn't find
    # a better way with pytest.


def test_close_commands_invoke_close_function(monkeypatch, capsys, sftp):
    """Tests that writing any valid close command at the program's main prompt,
    e.g. 'bye', 'exit', or 'quit', calls the close action.
    """

    # Replace the real close action with our mocked version.
    monkeypatch.setattr(close, "close", mock_close)

    # For each input, invoke the main loop with an open connection,
    # pass in the input, and verify that mock_close() was called.
    for input in INPUTS:
        with mock_input(input):
            main_loop(sftp)
            assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_close_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the close action."""

    # Pass a fake command to main_loop() and verify that it detects that the
    # command is not recognized. Note that main_loop() terminates because
    # it reaches EOF in our simulated stdin, so it's impractical for us to
    # monkeypatch mock_close in and verify that it was NOT called. Even if
    # we could prevent main_loop from calling it, we would prevent main_loop
    # from terminating, most likely, so our test would never conclude.
    with mock_input("sayonara"):
        main_loop(sftp)
        assert "not recognized" in capsys.readouterr().out
