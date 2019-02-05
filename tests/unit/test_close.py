from actions import close
from app import login
from tests.test_server import HOSTNAME, USERNAME, PASSWORD

def test_real_close():
    """Tests close() when logged onto an active, authentic connection. Ideal behavior
       is returning None type.
    """
    sftp = login.login(HOSTNAME,
                       USERNAME,
                       PASSWORD)
    assert close.close(sftp) is None


def test_close_with_invalid_credentials():
    """ Tests close() when NOT logged onto an active, authentic connection. Ideal behavior
         is returning an Exception with fake credentials.
    """
    try:
        sftp = login.login("FAKE", "FAKE", "FAKE")
        assert close.close(sftp) == Exception
    except Exception as error:
        return
