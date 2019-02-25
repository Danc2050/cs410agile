from actions import put_folder_on_remote_server as put_folder


def test_no_folder(sftp, capsys):
    """Test what happens when you ask to transfer a
    folder which doesn't exist.
    """

    assert put_folder.put_r(sftp, "fake") is False
    assert put_folder.ERROR_MESSAGE in capsys.readouterr().out

def test_best_case(sftp):
    """This tests what happens if you put a folder that does exist on
    to the remote server. This is the complex case -- 1) multiple files,
    multiple folders.
    """
    assert put_folder.put_r(sftp, "folder") is True
    # Cleanup of test case.
    sftp.remove("text.txt")
    sftp.remove("text2.txt")
    sftp.chdir("folder2")
    sftp.remove("f1.txt")
    sftp.remove("f2.txt")
    sftp.chdir("..")
    sftp.rmdir("folder2")
    sftp.chdir("..")
    sftp.rmdir("folder")

def test_permission(sftp, capsys):
    # Changes into the directory that we do not have permission to (/home)
    sftp.chdir("..")
    assert put_folder.put_r(sftp, "folder") is False
    assert put_folder.PERMISSION_ERROR in capsys.readouterr().out