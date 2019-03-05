from .input_handler import read_user_input
from actions import *
import pysftp
from actions import close
from actions import list_commands


# ===================
# SECTION: Controller
# ===================

ERROR_MESSAGE_NOT_RECOGNIZED = "That command is not recognized."


def main_loop(sftp: pysftp.Connection) -> int:
    """Main controller loop. Asks the user for input, attempts to decipher
    user input, and invoke the appropriate actions with the desired arguments.
    """

    # Main control loop.
    while True:
        # Catch disconnects, no connection errors, and pysftp's raised exceptions.
        try:
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
            if len(tokens) == 0:
                continue
            elif len(tokens) == 1 and tokens[0].lower() == "ls":
                list_files_remote.list_dir(sftp)
            elif len(tokens) == 2 and tokens[0] == "rm":
                # Using "rm" as remove
                remove_from_remote_server.remove_from_remote_server(sftp, tokens[1])
            elif len(tokens) == 1 and tokens[0] == "?":
                # If there is only one
                list_commands.list_commands()
            elif len(tokens) == 1 and tokens[0].lower() == "lls":
                list_files_local.display_local_files()
            elif len(tokens) == 3 and tokens[0].lower() == "chmod":
                # Change Permissions
                change_permissions_remote.change_permissions(sftp, tokens[1], tokens[2])
            elif len(tokens) == 2 and tokens[0] == "put":
                put_file_onto_remote_server.put(sftp, tokens[1])
            elif len(tokens) == 2 and tokens[0] == "get":
                get_file_from_remote_server.get(sftp, tokens[1])
            elif len(tokens) == 3 and tokens[0] == "rename":
                rename_file_remote.rename_remote_file(sftp, tokens[1], tokens[2])
            elif len(tokens) == 2 and tokens[0] == "mkdir":
                create_directory_on_remote.create_dir_remote(sftp, tokens[1])
            elif len(tokens) == 3 and tokens[0] == "lrename":
                rename_files_local.rename_local_file(tokens[1], tokens[2])
            elif len(tokens) == 3 and tokens[0] == "put" and tokens[1] == "-r":
                put_folder_on_remote_server.put_r(sftp, tokens[2])
            elif len(tokens) >= 2 and tokens[0] == "mput":
                put_multiple_files_onto_remote_server.put_multiple(sftp, tokens[1:])
            elif len(tokens) == 2 and tokens[0] == "rmdir":
                remove_directory_on_remote.remove_dir_remote(sftp, tokens[1])
            elif len(tokens) == 1 \
                    and (tokens[0].lower() == "exit"
                         or tokens[0].lower() == "bye"
                         or tokens[0].lower() == "quit"):
                #  User wants to exit
                print("\nConnection closed.")
                close.close(sftp)
                return 0
            else:
                print(ERROR_MESSAGE_NOT_RECOGNIZED)

        except AttributeError as e:
            if "open_session" in str(e):
                # The connection has been severed or a command was attempted
                # while no connection was active.
                print("The connection was closed unexpectedly.")
                return -1
            else:
                raise

        except OSError as e:
            # pysftp raises LOTS of OSErrors to communicate failed operations,
            # but the library and program are still in a valid state afterward,
            # so we can and should continue execution after displaying the
            # failure messages.
            #
            # Any actions that need to provide special handling of OSErrors
            # should catch OSError or appropriate subclasses and handle them
            # internally, leaving this catch-all for errors that simply need
            # to be displayed.
            print("Error:", e.strerror)
