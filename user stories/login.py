import pysftp

#username = "danc2"#input("Enter username.") -- Example
#password = "Sch00l21!"#input("Enter password.")  -- Example

#Connect to Server
def login(host, username, password):
    try:
        sftp = pysftp.Connection(host = 'linux.cs.pdx.edu', username=username, password=password)
    except Exception as error:
        print("Connection error message: " + error.args)
        return 0
    else:
        print("Authentication success.")
    return sftp