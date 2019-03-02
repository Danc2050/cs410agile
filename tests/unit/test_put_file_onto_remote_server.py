
from os import remove
import pysftp
import pytest
import paramiko
from actions import put_file_onto_remote_server as put


def test_no_file(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    with pytest.raises(OSError):
        put.put(sftp, "totes.not.fake.no.really")


def test_best_case(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """

    filename = "test_put_best_case"
    open(filename, "a").close()
    assert put.put(sftp, filename) is True
    remove(filename)
    sftp.remove(filename)


def test_put_file_when_exists_as_folder_prints_helpful_error_message(sftp, capsys):
    """If we upload a file 'foo' but a folder 'foo' already exists on remote,
    pysftp raises an OSError with no error message, which isn't helpful. To
    avoid printing the unhelpful 'Error: None' that would be produced by default,
    the put action should check whether 'foo' is a folder and display a custom
    error message. Otherwise, it should re-raise the error. This test verifies
    that put prints said error message and returns False.
    """

    filename = "test_put_file_when_exist_as_folder"

    # Set up our test case
    open(filename, "a").close()
    sftp.makedirs(filename)

    assert put.put(sftp, filename) is False
    assert put.FOLDER_CONFLICT_ERROR_MESSAGE in capsys.readouterr().out

    # Clean up our test case
    remove(filename)
    sftp.rmdir(filename)
