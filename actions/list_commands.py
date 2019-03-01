

def list_commands():
    print(
        # Note to developers: please sort alphabetically for ease of use
        # and please adjust spacing as needed.
        "bye\t\tclose the connection and exit\n"
        "exit\t\tclose the connection and exit\n"
        "lls\t\tlist files on local machine\n"
        "put file\tput a file onto server\n"
        "put -r folder\tput a folder onto server recursively\n"
        "quit\t\tclose the connection and exit\n"
        "rm file\t\tremove file\n"
    )
    return True
