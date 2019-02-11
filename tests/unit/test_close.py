from actions import close
from app import login
from tests.test_server import HOSTNAME, USERNAME, PASSWORD


def test_real_close():
    """Tests close() when logged onto an active, authentic connection.
    Ideal behavior is returning None type.
    """
    sftp = login.login(HOSTNAME,
                       USERNAME,
                       PASSWORD)
    assert close.close(sftp) is None
