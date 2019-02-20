from actions import put_folder_on_remote_server as put_folder


def test_no_folder(sftp, capsys):
    """Test what happens when you ask to transfer a
    folder which doesn't exist.
    """

    assert put_folder.put_r(sftp, "fake") is False
    #assert put_folder.ERROR_MESSAGE in capsys.readouterr().out # Does not work.

def test_best_case(sftp):
    """This tests what happens if you put a folder that does exist on
    to the remote server
    """
    assert put_folder.put_r(sftp, "folder") is True
