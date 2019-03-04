import os


def display_local_files():
    """
            Method to display the files in current directory.
    """

    for entry in os.listdir("."):
        if not entry.startswith('.'):
            print(entry, end='    ')
    print()

