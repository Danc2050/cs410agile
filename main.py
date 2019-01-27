from app import controller
import pysftp
import sys
from actions import login

if __name__ == "__main__":

    # Login attempt
    sftp = login.login()
    # Type test for valid pysftp.Connection object
    try:
        if type(sftp) == pysftp.Connection:
            # Run the main controller loop, and when it returns, pass along its
            # return value as the program's exit code.
            sys.exit(controller.main_loop(sftp))
    except Exception as error:
        print("pysftp object allocation error message: " + error.args)
        sys.exit(1)