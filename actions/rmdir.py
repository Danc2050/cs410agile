#Remove Directory
import pysftp

usage = "Error: no such file"

def rmdir(sftp, directory):
    try:
        print("wait...")
        listCurrentDirPath = sftp.execute("pwd")
        current = str(listCurrentDirPath[0])
        current = current[2:-3]
        current = 'rm -r ' + current + '/' + directory
        sftp.execute(current)
        return True
    except IOError:
        print(useage)
        return False
