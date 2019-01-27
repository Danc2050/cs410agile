from app import controller
from actions import login
import pysftp
import sys
import getpass
from tests import test_server

if __name__ == "__main__":
    # Type test for valid pysftp.Connection object
    try:
        # Login attempt
        len(sys.argv[1]) == 2
        tup = sys.argv[2].split("@")
        hostname = tup[0]
        username = tup[1]
        print(hostname+"@"+username+"'s", end=' ', flush=True)
        password = getpass.getpass()
        print(password)
        sftp = login.login(hostname, username, password)

        # Type check
        if type(sftp) == pysftp.Connection:
            print("Authentication success.")
       # Run the main controller loop, and when it returns, pass along its
        # return value as the program's exit code.
        sys.exit(controller.main_loop(sftp))
    except Exception as error:
        print("pysftp object allocation error message: " + str(error.args))
        sys.exit(1)