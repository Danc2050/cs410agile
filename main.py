from app import controller, login
import pysftp
import sys
import getpass

INVALID_ARGUMENT_MESSAGE = \
    "Invalid arguments. Please specify either hostname or user@hostname."

if __name__ == "__main__":

    # TODO Write comment here
    try:

        # Check that we received exactly one command-line argument.
        if len(sys.argv) != 2:
            print(INVALID_ARGUMENT_MESSAGE)
            exit(1)

        # Split our one argument on "@", which will either give us
        # a username and a hostname or just a hostname (if there is no "@").
        tup = sys.argv[1].split("@")

        if len(tup) > 2 or len(tup) == 0:
            # The user didn't pass in user@hostname or hostname, so we
            # can't proceed. We'll print the correct invocation and exit
            # so they can try again.
            print(INVALID_ARGUMENT_MESSAGE)
            exit(1)

        if len(tup) == 2:
            # The user passed in user@hostname, so tup = [user, hostname].
            username = tup[0]
            hostname = tup[1]

        else:  # len(tup) == 1
            # The user passed in hostname only, so we'll retrieve
            # the currently logged-in username from the OS.
            username = getpass.getuser()
            hostname = sys.argv[1]

        # Print username@hostname and prompt for password.
        # getpass.getpass() does not echo the input, as a security measure
        #
        # Note: if you run through PyCharm, getpass() may behave very oddly.
        # It should work correctly from the terminal, though.
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
        print(error)
        sys.exit(1)
