#Remove Directory
import pysftp

usage = "Error: no such file or directory contains content at "

# Remove directory on server
def rmdir(sftp, directory):
    try:
        listCurrentDir = sftp.pwd                         # extract the current directory string from list
        #fullpath = listCurrentDir + "/" + directory       # create a string of command rm -r /u/../directory
        #sftp.rmdir(directory)
        print('rm -rf ' + directory)
        sftp.execute('rm -rf ' + directory)
        return True
    except OSError as e:
        if e.strerror is None:
            print("Could not remove directory.")
        else:
            print("Error:", e.strerror)
        return False

# end
