from actions import listdir as listD
import pytest
import paramiko
from paramiko import sftp_client


def test_list(sftp, capsys):
    """Each users folder will be different. Therefore, we must test for a file that we know.
       Does the list return what's actually there? We may test for one file that we absolutely
       know exists (e.g., 'emacs', line 16).
       Additionally, these are the (hidden) files that all "Dylan" servers should have in common:
       ['.bash_logout', '.bash_profile', '.bashrc', '.emacs', '.kshrc', '.zshrc'].
       We could test for every file in this list being in the loop if we wanted to guarantee that
       such a list exists.
    """

    # Test file and folder that should be listed
    file = 'fakeFile'
    folder = 'listFolder'

    # Create the file and folder
    sftp.open(file, "a").close()
    sftp.makedirs(folder)

    # Retrieve our listing
    listD.list_dir(sftp)

    # Clean up after ourselves before asserting, since a failed assertion will stop the test and prevent clean-up
    sftp.rmdir(folder)
    sftp.remove(file)

    # Then check whether we listed the test file and folder.
    output = capsys.readouterr().out
    assert file in output
    assert folder in output

def test_permission(sftp):
    # Changes into the directory that we do not have permission to (/home)
    sftp.chdir("..")
    with pytest.raises(OSError):
        listD.list_dir(sftp)
