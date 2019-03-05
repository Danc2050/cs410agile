import os
import pysftp

from actions import put_multiple_files_onto_remote_server as mput, \
    put_file_onto_remote_server as put


def test_no_file(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    files = ["totes.not.fake.no.really", "another.fake"]
    assert mput.put_multiple(sftp, files) is False
    assert mput.ERROR_MESSAGE in capsys.readouterr().out


def test_best_case(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """

    # Create file locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    f = open('test2.txt', 'w')
    f.write('testing')
    f.close()

    files = ["test.txt", "test2.txt"]
    assert mput.put_multiple(sftp, files) is True

    # Remove local files
    os.remove('test.txt')
    os.remove('test2.txt')

    # Remove remote files
    sftp.remove('test.txt')
    sftp.remove('test2.txt')


def test_best_case_single(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """

    # Create file locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    files = ["test.txt"]
    assert mput.put_multiple(sftp, files) is True

    # Remove local files
    os.remove('test.txt')

    # Remove remote files
    sftp.remove('test.txt')


def test_some_valid_files(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server, but also one that doesn't exist
    """

    # Create file locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    files = ["test.txt", "not.a.real.file"]
    assert mput.put_multiple(sftp, files) is True

    # Remove local files
    os.remove('test.txt')

    # Remove remote files
    sftp.remove('test.txt')

def test_mput_catches_exceptions(sftp, capsys, monkeypatch):
    """This test verifies that the put_multiple action correctly catches
    OSError exceptions that put might raise and continues on.
    """

    # List of files that should succeed
    goodFiles = ["mput_good", "mput_great"]

    # List of files to attempt to mput, in the pattern: badfile, goodfile, ...
    files = ["mput_bad", "mput_good", "mput_fail", "mput_great"]

    def mock_put(sftp: pysftp.Connection, filename: str):
        """A mocked put() function that prints good filenames so we can
        test against them and raises OSErrors for bad filenames so we can be
        sure they're caught."""
        if filename in goodFiles:
            print(filename)
        else:
            raise OSError("mock_put: filename = " + filename)

    monkeypatch.setattr(put, "put", mock_put)

    mput.put_multiple(sftp, files)

    output = capsys.readouterr().out
    for file in files:
        assert file in output
