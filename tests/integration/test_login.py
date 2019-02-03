import app
import getpass
from main import main
import paramiko
import pysftp
import pytest
import sys
from tests import test_server


def test_login_with_various_credentials(monkeypatch):
    """Test that main() calls login() and succeeds or fails depending on
    whether the provided credentials are valid. (Note that it's not the
    integration test's job to check all input cases, only to verify that
    the modules are wired together correctly.
    """

    # SECTION: test setup.

    # Our magic return value.
    RETVAL = 42

    # Define a fake controller that just returns a known value
    # instead of looping around.
    def mock_controller(sftp: pysftp.Connection) -> int:
        return RETVAL

    # Replace the real controller with this one for this test.
    monkeypatch.setattr(app.controller, 'main_loop', mock_controller)

    # Mock the password request.
    def mock_getpass():
        return test_server.PASSWORD
    monkeypatch.setattr(getpass, 'getpass', mock_getpass)

    # Backup original argv
    original_argv = sys.argv

    # SECTION: test 1 - successful login.

    # Set up fake argv.
    sys.argv = ['main.py', test_server.USERNAME + '@' + test_server.HOSTNAME]

    # Verify that, on successful login, the controller returns RETVAL
    with pytest.raises(SystemExit) as e:
        main()
        assert e.type == SystemExit
        assert e.value.code == RETVAL

    # SECTION: test 2 - unsuccessful login.

    # Set up fake argv.
    sys.argv = ['main.py', 'cs510fakeuser@' + test_server.HOSTNAME]

    # Verify that main() returns a non-zero return code.
    with pytest.raises(SystemExit) as e:
        main()
        assert e.type == SystemExit
        assert e.value.code != 0

    # SECTION: teardown.

    # Return argv to its original value
    sys.argv = original_argv
