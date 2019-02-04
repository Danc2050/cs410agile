from .input_handler import read_user_input
import pysftp
from actions import close


# ===================
# SECTION: Controller
# ===================


def main_loop(sftp: pysftp.Connection) -> int:
    """Main controller loop. Asks the user for input, attempts to decipher
    user input, and invoke the appropriate actions with the desired arguments.
    """

    # Catch disconnects & no connection errors.
    try:
        # Main control loop.
        while True:

            # First, we take in a command sequence from the user.
            try:
                tokens = read_user_input()
            except EOFError:
                # EOF received. User wants to close the program.
                print("\nConnection closed.")
                close.close(sftp)
                return 0

            # ==========================
            # LIST OF SUPPORTED ACTIONS: add new actions as elif clauses.
            # ==========================

            # Blank line. Ignore.
            # TODO We may want to consider using .lower() to make commands case insensitive.
            if len(tokens) == 0:
                continue
            elif len(tokens) == 1 and tokens[0].lower() == "ls":
                # Barebones remote "ls" support to let us write meaningful
                # tests of the basic skeleton.
                # TODO Replace this action handler when implementing remote ls.
                sftp.listdir(".")

            # TODO Manual testing for each string is complete. However, do we want to make it a test?
            elif len(tokens) == 1 and tokens[0].lower() == "exit" or tokens[0].lower() == "bye" or tokens[0].lower() == "quit":
                #  User wants to exit
                print("\nConnection closed.")
                close.close(sftp)
                return
            else:
                print("That command is not recognized.")

    except AttributeError as e:
        if "open_session" in str(e):
            # The connection has been severed or a command was attempted
            # while no connection was active.
            print("The connection was closed unexpectedly.")
            return -1
        else:
            raise