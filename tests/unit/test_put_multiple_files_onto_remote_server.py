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

    files = ["main.py", "README.md"]
    assert put.put_multiple(sftp, files, len(files)) is True

