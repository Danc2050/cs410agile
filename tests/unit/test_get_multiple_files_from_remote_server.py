import os

from actions import get_multiple_files_from_remote_server as get


def test_no_files(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    files = ["totes.not.fake.no.really", "another.fake"]
    assert get.get_multiple(sftp, files) is False
    assert get.ERROR_MESSAGE in capsys.readouterr().out


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
    assert get.get_multiple(sftp, files) is True

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
    assert get.get_multiple(sftp, files) is True

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
    assert get.get_multiple(sftp, files) is True

    # Remove local files
    os.remove('test.txt')

    # Remove remote files
    sftp.remove('test.txt')
