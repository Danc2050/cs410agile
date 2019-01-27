from app import controller
from actions import login
import pysftp
import sys
import getpass
from tests import test_server

if __name__ == "__main__":
    hostname = 0
    username = 0
    # Type test for valid pysftp.Connection object
    try:
        # Login attempt
        if len(sys.argv) != 2:
            print("# of arguments not satisfied.")
        tup = sys.argv[1].split("@")
        if(len(tup) == 2): # if .split fails, then tup should == sys.argv
            username = getpass.getuser()
            print(username)
        else:
            hostname = tup[1]
            username = tup[0]
        print(username+"@"+hostname, end=' ', flush=True)
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