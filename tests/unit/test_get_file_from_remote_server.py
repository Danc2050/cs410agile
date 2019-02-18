from actions import get_file_from_remote_server as get


def test_no_file(sftp, capsys):
    """Test what happens when you ask to transfer a
    file which doesn't exist.
    """

    assert get.get(sftp, "totes.not.fake.no.really") is False
    assert get.ERROR_MESSAGE in capsys.readouterr().out


def test_best_case(sftp):
    """This tests what happens if you get a file that does exist on
    the remote server
    """

    # Create file locally
    f = open('test.txt', 'w')
    f.write('testing')
    f.close()

    # Put file on the remote server
    sftp.put('test.txt', 'test.txt', preserve_mtime=False)

    # Test getting file
    assert get.get(sftp, "test.txt") is True
