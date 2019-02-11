import pysftp
import pytest
from tests.test_server import *


@pytest.fixture(scope="function")
def sftp():
    """This fixture provides a pysftp.Connection object that's shared
    across the entire tests package. If there's a problem connecting,
    it will raise an exception that will terminate testing."""
    return pysftp.Connection(
        host=HOSTNAME,
        username=USERNAME,
        password=PASSWORD
    )
