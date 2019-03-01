from actions import put_folder_on_remote_server as put_folder, \
    put_file_onto_remote_server as put_file
from app.controller import main_loop
from os import remove
from pathlib import Path
import pysftp
from tests.test_helpers import mock_input

# Arbitrary string that we'll print inside mock_put()
# and check for in our tests.
SUCCESS_STRING = "mock_put_r CALLED"

# The fake filename to pass in.
FOLDER = "testfolder"


def mock_put_r(sftp: pysftp.Connection, folder: str):
    """A fake rename_local_file() function that checks the arguments and prints
    a string we can check for, to verify that the function was called.
    """

    assert isinstance(sftp, pysftp.Connection)
    assert folder == FOLDER
    print(SUCCESS_STRING)


def test_put_r_invokes_put_folder_action(capsys, monkeypatch, sftp):
    """Tests that writing text like 'lrename from to' calls the put action and
    passes 'from' as the original filename and 'to' as the new filename.
    """

    # Replace the real action with our mocked function
    monkeypatch.setattr(put_folder, "put_r", mock_put_r)

    # Pass in a valid input
    with mock_input("put -r {}".format(FOLDER)):
        main_loop(sftp)

    assert SUCCESS_STRING in capsys.readouterr().out


def test_invalid_commands_do_not_invoke_put_r_function(capsys, sftp):
    """Tests that writing invalid commands doesn't invoke the rename action."""

    # Test inputs. They need to be a single sequence, or we'll send EOF
    # and close our SFTP connection after the first test.
    test_inputs = """doesnotexist
                     put -r 
                     put -r ham sandwich"""
    for test in test_inputs:
        with mock_input(test):
            main_loop(sftp)
            assert SUCCESS_STRING not in capsys.readouterr().out


def test_put_r_with_file_invokes_put_action(monkeypatch, sftp):
    """Tests that writing 'put -r file' where file is a filename rather
    than a folder name actually invokes the put_file_onto_remote_server
    action."""

    def mock_put_file(sftp, filename):
        return SUCCESS_STRING

    # Replace the real action with our mocked function
    monkeypatch.setattr(put_file, "put", mock_put_file)

    # Supposing it's a file....
    monkeypatch.setattr(Path, "is_file", lambda slf: True)

    assert put_folder.put_r(sftp, "test_file") == SUCCESS_STRING
