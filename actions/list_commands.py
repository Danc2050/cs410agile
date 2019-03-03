def list_commands():
    print(
        # Note to developers: please sort alphabetically for ease of use
        # and please adjust spacing as needed.
        "bye\t\t\tclose the connection and exit\n"
        "exit\t\t\tclose the connection and exit\n"
        "lls\t\t\tlist files on local machine\n"
        "lrename old new\t\trenames a file or folder from old to new\n"
        "ls\t\t\tlist files on remote machine\n"
        "mkdir dir\t\tcreate a directory named dir on remote server\n"
        "put file\t\tput a file onto server\n"
        "put -r folder\t\tput a folder onto server recursively\n"
        "quit\t\t\tclose the connection and exit\n"
        "rename old new\t\trename file on remote server from old to new\n"
        # "rm file\t\t\tremove file\n"
    )
    return True
