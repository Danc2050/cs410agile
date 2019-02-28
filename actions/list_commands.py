

def list_commands():
    print(
        # Note to developers: please sort alphabetically for ease of use
        # and please adjust spacing as needed.
        "lls\t\tlist files on local machine\n"
        "put file\tput a file onto server\n"
        "put -r folder\tput a folder onto server recursively\n"
        "rm file\t\tremove file\n"
    )
    return True
