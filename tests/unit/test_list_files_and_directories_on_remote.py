from actions import listdir as listD


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
    for file in listD.list_dir(sftp):
        if file == '.emacs':
            file_exists = True
    assert file_exists is True