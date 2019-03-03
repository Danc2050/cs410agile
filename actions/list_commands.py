def list_commands():
    print(
        # Note to developers: please sort alphabetically for ease of use
        # and please adjust spacing as needed.
        "bye\t\t\tclose the connection and exit\n"
        "exit\t\t\tclose the connection and exit\n"
        "lls\t\t\tlist files on local machine\n"
        "lrename old new\t\trenames a file or folder from old to new\n"
        "ls\t\t\tlist files on remote machine\n"
        "put file\t\tput a file onto server\n"
        "get file\t\tget a file from the server\n"
        "mget file file ...\t\tgets multiple files from the server\n"
        "put -r folder\t\tput a folder onto server recursively\n"
        "quit\t\t\tclose the connection and exit\n"
        # "rm file\t\t\tremove file\n"
    )
    return True
