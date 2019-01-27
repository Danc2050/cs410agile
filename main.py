from app import controller
from actions import login
import pysftp
import sys
import getpass

if __name__ == "__main__":

    # Type test for valid pysftp.Connection object
    try:

        # Login attempt
        if len(sys.argv) != 2:
            print("Incorrect sftp command.")
            exit(1)
        tup = sys.argv[1].split("@")
        if(len(tup) == 2): # if .split fails, then
            hostname = tup[1]
            username = tup[0]
        else:
            username = getpass.getuser()
            hostname = sys.argv[1]

        # Printing credentials and asking for password
        print(username+"@"+hostname+"'s", end=' ', flush=True)
        password = getpass.getpass()
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