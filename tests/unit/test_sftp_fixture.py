def test_close_sftp(sftp):
    """Closes the SFTP connection so that future tests can verify that they get a fresh sftp object."""
    sftp.close()

def test_sftp_fixture_is_function_scoped(sftp):
    """Tests that the sftp object is fresh for this function."""

    sftp.listdir('.')
