from actions import rmdir

# TEST 1: Directory exists


def test_delete_empty_directory_succeeds(sftp):

    directory = "test_delete_empty_directory_succeeds"
    sftp.mkdir(directory, mode=777)                 # add a directory
    assert rmdir.rmdir(sftp, directory) is True     # remove directory
    # Cleanup
    rmdir.rmdir(sftp, directory)

# TEST 2: Directory does not exist


def test_delete_non_exisitance_directory_fail(sftp):
    directory = "test_no_directory_fail"
    assert rmdir.rmdir(sftp, directory) is False
    # Cleanup
    rmdir.rmdir(sftp, directory)

# TEST 3: Directory has content


def test_del_directory_with_content(sftp):
    directory1 = "test_content_directory_fail"
    directory2 = "test_content_directory_fail/test"
    sftp.mkdir(directory1, mode=777) # Create a directory
    sftp.mkdir(directory2, mode=777) # Create a sub-directory
    assert rmdir.rmdir(sftp, directory1) is False   # test delete directory which has content in it ("test")
    # Cleanup
    rmdir.rmdir(sftp, directory2)
    rmdir.rmdir(sftp, directory1)
