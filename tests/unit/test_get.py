from actions import close
from app import login
from tests.test_server import HOSTNAME, USERNAME, PASSWORD
from actions import get

def test_real_get():
    """Tests sftp.get() when logged onto an active, authentic connection. Ideal behavior
       is .
    """
    sftp = sftp()
    login.login(HOSTNAME,
                       USERNAME,
                       PASSWORD)
    assert close.close(sftp) is None


def test_get_with_invalid_paths():
    """ Tests close() when NOT logged onto an active, authentic connection. Ideal behavior
         is returning an Exception with fake credentials.
    """

    try:
        sftp = login.login("FAKE", "FAKE", "FAKE")
        assert close.close(sftp) == Exception
    except Exception as error:
        return
