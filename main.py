from app import controller, login
from io import StringIO
import pysftp
import sys
import getpass

INVALID_ARGUMENT_MESSAGE = \
    "Invalid arguments. Please specify either hostname or user@hostname."


def main():
    # Catch-all try block for attempting to run the program.
    try:

        # Check that we received exactly one command-line argument.
        if len(sys.argv) != 2:
            print(INVALID_ARGUMENT_MESSAGE)
            return 1

        # Split our one argument on "@", which will either give us
        # a username and a hostname or just a hostname (if there is no "@").
        tup = sys.argv[1].split("@")

        if len(tup) > 2 or len(tup) == 0:
            # The user didn't pass in user@hostname or hostname, so we
            # can't proceed. We'll print the correct invocation and exit
            # so they can try again.
            print(INVALID_ARGUMENT_MESSAGE)
            return 1

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
            return controller.main_loop(sftp)

    except Exception as error:
        print(error)

        # Disable exception printing before exit. Note: this is super-janky
        # and should never be used unless the program is about to close!
        # We just flatly replace the standard error output with a buffer
        # that we never read.
        #
        # We have to do this because pysftp raises an exception during
        # teardown if it was passed garbage inputs like hamsandwich@beepboop.
        # If we don't disable exception printing, Python prints a stack trace
        # for an ignored exception. Why? We can't catch the exception,
        # because when it's raised, we've already called sys.exit(), so
        # we don't have any code in scope. There's nowhere for the exception
        # to go.
        sys.stderr = StringIO()

        return 1


if __name__ == "__main__":
    sys.exit(main())
