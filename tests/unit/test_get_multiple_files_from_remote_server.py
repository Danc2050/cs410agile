import os
import pysftp
from actions import get_multiple_files_from_remote_server as mget, \
    get_file_from_remote_server as get


def test_no_files(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    files = ["totes.not.fake.no.really", "another.fake"]
    assert mget.get_multiple(sftp, files) is False
    assert mget.ERROR_MESSAGE in capsys.readouterr().out


def test_best_case(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """

    files = ['test.txt', 'test2.txt']

    # Create files locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    f = open('test2.txt', 'w')
    f.write('testing2')
    f.close()

    # Put files on the remote server
    sftp.put('test.txt', 'test.txt', preserve_mtime=False)
    sftp.put('test2.txt', 'test2.txt', preserve_mtime=False)

    # Test getting files
    assert mget.get_multiple(sftp, files) is True

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

    files = ['test.txt']

    # Create files locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    # Put files on the remote server
    sftp.put('test.txt', 'test.txt', preserve_mtime=False)

    # Test getting files
    assert mget.get_multiple(sftp, files) is True

    # Remove local files
    os.remove('test.txt')

    # Remove remote files
    sftp.remove('test.txt')


def test_some_good_files(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server
    """

    files = ['test.txt', 'test2.txt']

    # Create files locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    # Put files on the remote server
    sftp.put('test.txt', 'test.txt', preserve_mtime=False)

    # Test getting files
    assert mget.get_multiple(sftp, files) is True

    # Remove local files
    os.remove('test.txt')

    # Remove remote files
    sftp.remove('test.txt')

def test_mget_catches_exceptions(sftp, capsys, monkeypatch):
    """This test verifies that the get_multiple action correctly catches
    OSError exceptions that get might raise and continues on.
    """

    # List of files that should succeed
    goodFiles = ["mget_good", "mget_great"]

    # List of files to attempt to mget, in the pattern: badfile, goodfile, ...
    files = ["mget_bad", "mget_good", "mget_fail", "mget_great"]

    def mock_get(sftp: pysftp.Connection, filename: str):
        """A mocked put() function that prints good filenames so we can
        test against them and raises OSErrors for bad filenames so we can be
        sure they're caught."""
        if filename in goodFiles:
            print(filename)
        else:
            raise OSError("mock_get: filename = " + filename)

    monkeypatch.setattr(get, "get", mock_get)

    mget.get_multiple(sftp, files)

    output = capsys.readouterr().out
    for file in files:
        assert file in output
