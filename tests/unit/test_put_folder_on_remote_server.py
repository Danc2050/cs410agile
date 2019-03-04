from actions import put_folder_on_remote_server as put_folder
from os import makedirs, remove, rmdir


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

    # Create folder structure for test, without throwing errors if the
    # folders already exist.
    folders = [
        "folder",
        "folder/folder2"
    ]
    for folder in folders:
        makedirs(folder, exist_ok=True)

    # Create files for test (if they don't already exist).
    files = [
        "folder/test.txt",
        "folder/test2.txt",
        "folder/folder2/f1.txt",
        "folder/folder2/f2.txt"
    ]
    for file in files:
        open(file, "a").close()

    assert put_folder.put_r(sftp, "folder") is True

    # Clean up local and remote files.
    for file in files:
        print(sftp.pwd, file)   # Print for debugging in case test fails.
        sftp.remove(file)
        remove(file)
    for folder in reversed(folders):
        print(sftp.pwd, folder)     # Print for debugging in case test fails.
        rmdir(folder)           # Succeeds even if the folder doesn't exist.
        sftp.rmdir(folder)


def test_permission(sftp, capsys):
    # Changes into the directory that we do not have permission to (/home)
    sftp.chdir("..")
    assert put_folder.put_r(sftp, "folder") is False
    assert put_folder.PERMISSION_ERROR in capsys.readouterr().out
