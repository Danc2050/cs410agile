from app import controller
from actions import login
import pysftp
import sys
from tests import test_server

if __name__ == "__main__":

    # Login attempt
    sftp = login.login(test_server.HOSTNAME, test_server.USERNAME, test_server.PASSWORD)
    # Type test for valid pysftp.Connection object
    try:
        if type(sftp) == pysftp.Connection:
            # Run the main controller loop, and when it returns, pass along its
            # return value as the program's exit code.
            sys.exit(controller.main_loop(sftp))
    except Exception as error:
        print("pysftp object allocation error message: " + error.args)
        sys.exit(1)