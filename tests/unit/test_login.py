import pysftp
from app import login
from tests.test_server import HOSTNAME, USERNAME, PASSWORD
import pytest
import paramiko


def test_real_login():
    """Tests login() with test_server credentials, which should result
    in a successful connection.
    """

    sftp = login.login(HOSTNAME,
                       USERNAME,
                       PASSWORD)
    assert type(sftp) is pysftp.Connection


def test_login_with_invalid_credentials(capsys):
    """Verify that calling login() with invalid credentials fails."""

    # List of test cases. Each case is of the form:
    #
    #   (host, username, password)
    test_cases = [
        (None, None, None),
        ("", "", ""),
        ("Fake", "Fake", "Fake"),
        (HOSTNAME, "Fake", "Fake"),
        (HOSTNAME, "cs510andrew", "zFa8FkS7CC7eG8fx"),  # Using Anthony's PW
        ("linuxlab.cs.pdx.edu", USERNAME, PASSWORD),
        ("sandwich dot com", USERNAME, PASSWORD),
        ("test@example.com", USERNAME, PASSWORD)
    ]

    # For each test case, verify that the same exception is raised.
    for host, username, password in test_cases:
        with pytest.raises(paramiko.ssh_exception.SSHException):
            login.login(host=host, username=username, password=password)
