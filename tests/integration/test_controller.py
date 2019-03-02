from actions import put_file_onto_remote_server
from app.controller import main_loop, ERROR_MESSAGE_NOT_RECOGNIZED
from tests.test_helpers import mock_input


def test_controller_continues_after_oserror(sftp, monkeypatch, capsys):
    """This test verifies that the controller prints an OSError message
    when it receives it and then continues execution (rather than quitting).
    """

    oserror_message = "THIS IS A TEST"

    def mock_put(s, f):
        """A mock put action that simply raises a known exception."""

        raise OSError(1, oserror_message)

    # Patch in our mocked put function.
    monkeypatch.setattr(put_file_onto_remote_server, "put", mock_put)

    # Our strategy here is to invoke two actions: our mock put, then an
    # invalid command. This will allow us to test for correct behavior, because
    # the controller will print its error message for unrecognized commands
    # if and only if it continues execution after handling the OSError.

    inputs = """
             put file
             hooligan town banana republic
             """
    with mock_input(inputs):
        main_loop(sftp)
        output = capsys.readouterr().out
        assert oserror_message in output

        # Now, we want to ensure that the error for unrecognized commands
        # is displayed AFTER the message we just asserted. So we'll split
        # the output on the message and check the second half.

        assert ERROR_MESSAGE_NOT_RECOGNIZED in \
            output.split(oserror_message, 1)[1]
