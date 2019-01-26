from app import controller
import pysftp
import sys
from tests import test_server

if __name__ == "__main__":

    # TODO Login logic goes here!
    # Temporary login logic - hard-coded to test server.
    sftp = pysftp.Connection(
        host=test_server.HOSTNAME,
        username=test_server.USERNAME,
        password=test_server.PASSWORD
    )

    # Run the main controller loop, and when it returns, pass along its
    # return value as the program's exit code.
    sys.exit(
        # FIXME Once login is implemented, pass in the correct pysftp object!
        controller.main_loop(sftp)
    )

