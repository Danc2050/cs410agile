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
            print("Sftp program must take one valid argument.")
            exit(1)

        # Edge case for splitting the destination address if an '@'
        # sign exists
        tup = sys.argv[1].split("@")

        # If .split succeeds, a '@' is in the sftp destination
        # and then the tuple returned will be {[user], [hostname]}
        # Set each respective field to a local variable
        if len(tup) == 2:
            hostname = tup[1]
            username = tup[0]

        # Otherwise, we need to get the host machines USER variable for username.
        # The hostname will be inside sys.argv[1] (e.g., dylanlaufenberg.com)
        else:
            username = getpass.getuser()
            hostname = sys.argv[1]

        # Printing credentials to user and asking for password from user
        # getpass.getpass() does not echo the input... a security measure
        print(username+"@"+hostname+"'s", end=' ', flush=True)
        password = getpass.getpass()
        sftp = login.login(hostname, username, password)

        # Type check for correct allocation of pysftp.Connection object
        if type(sftp) == pysftp.Connection:
            print("Authentication success.")
            # Run the main controller loop, and when it returns, pass along its
            # return value as the program's exit code.
            sys.exit(controller.main_loop(sftp))

    except Exception as error:
        print("pysftp object allocation error message: " + str(error.args))
        sys.exit(1)