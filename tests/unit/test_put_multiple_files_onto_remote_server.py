import os

from actions import put_multiple_files_onto_remote_server as put


def test_no_file(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    files = ["totes.not.fake.no.really", "another.fake"]
    assert put.put_multiple(sftp, files, len(files)) is False
    assert put.ERROR_MESSAGE in capsys.readouterr().out


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
    assert put.put_multiple(sftp, files, len(files)) is True

    os.remove('test.txt')
    os.remove('test2.txt')


def test_some_valid_files(sftp):
    """This tests what happens if you put a file that does exist on
    to the remote server, but also one that doesn't exist
    """

    # Create file locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    files = ["test.txt", "not.a.real.file"]
    assert put.put_multiple(sftp, files, len(files)) is True

    os.remove('test.txt')


