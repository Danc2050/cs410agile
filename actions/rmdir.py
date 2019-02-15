#Remove Directory
import pysftp

usage = "Error: no such file"

# Remove directory on server
def rmdir(sftp, directory):
    try:
        print("working...")
        listCurrentDir = sftp.execute("pwd")
        current = str(listCurrentDir[0])
        current = current[2:-3]                          # extract the current directory string from list
        current = 'rm -r '+ current + '/' + directory    # create a string of command rm -r /u/../directory
        sftp.execute(current)                            # run command
        return True
    except IOError:
        print(usage)
        return False

# end
