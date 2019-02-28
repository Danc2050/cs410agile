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

    file_exists = False
    folder_exists = False
    sftp.makedirs('listFolder')
    for file in listD.list_dir(sftp):
        if file == '.emacs':
            file_exists = True
        if file == 'listFolder':
            folder_exists = True
    sftp.rmdir('listFolder')
    assert file_exists is True
    assert folder_exists is True

def test_permission(sftp):
    # Changes into the directory that we do not have permission to (/home)
    sftp.chdir("..")
    with pytest.raises(paramiko.sftp_client.SFTP_PERMISSION_DENIED):
        listD.list_dir(sftp)
#assert listD.list_dir(sftp) PermissionError
#    raise IOError(errno.EACCES, text)
