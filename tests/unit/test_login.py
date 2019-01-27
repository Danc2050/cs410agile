import pysftp
from actions import login
from tests import test_server

# Login with test_server credentials (should work if file is loaded)
def test_real_login():
    assert type(login.login(test_server.HOSTNAME, test_server.USERNAME, test_server.PASSWORD)) is pysftp.Connection
# Login without proper credentials
def test_fake_login():
    assert type(login.login("Fake", "Fake", "Fake")) is not pysftp.Connection