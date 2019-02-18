#Remove Directory
import pysftp

usage = "Error: no such file or directory contains content at "

# Remove directory on server
def rmdir(sftp, directory):
    try:
        listCurrentDir = sftp.pwd                         # extract the current directory string from list
        fullpath = listCurrentDir + "/" + directory       # create a string of command rm -r /u/../directory
        #sftp.execute("rmdir -r " + fullpath)             # unstable command (ignore)
        sftp.rmdir(directory)

        return True
    except IOError:
        print(usage + sftp.pwd + "/" + directory)
        return False

# end
