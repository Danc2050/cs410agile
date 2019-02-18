from app import controller, login
from io import StringIO
import pysftp
import sys
import rmdir
#import actions import *   # Unable to import

#from tests.test_server import test_server
#from tests import test_server

HOSTNAME = "dylanlaufenberg.com"
USERNAME = "cs510andrew"
PASSWORD = "5Jq7hHjVZqPwaMU3"

# TEST 1: Directory exists
def del_existing_dir(test_connection, directory):
    try:
        test_connection.mkdir(directory, mode=777)                 # add a directory
        test_connection.rmdir(directory)
        return test_connection.listdir()
    except IOError
        return IOError

# TEST 2: Directory does not exist
def del_no_existing_file(test_connection, directory):
    try:
        test_connection.rmdir(directory)
        return True
    except IOError:
        return IOError

# TEST 3: Directory has content
def content_dir(test_connection, directory):
    try:
        test_connection.mkdir(directory, mode=777)  # add a directory
        f = open(directory +".txt", "w+")
        f.close()

        remotePath = test_connection.pwd + "/" + directory + "/" + directory +".txt"
        test_connection.put(directory + ".txt",remotePath )

        test_connection.rmdir(directory)
        return True
    except IOError:
        return IOError

# Testing method
def test(got, expected):
    if got == expected:
        prefix = "OK"
    else:
        prefix = "X"
    print(prefix, "got: ", got, " expected: ", expected)


def main():
    sftp = pysftp.Connection(host=HOSTNAME, username=USERNAME, password=PASSWORD)

    #Unit Tests
    print("Unit Test: rmdir method")

    # 1 Test deleting an existing empty directory
    #    create file and delete file
    #    Successful return matching directory listing as before and after
    print('TEST 1: Directory exists')
    test(del_existing_dir(sftp, "Test12345"), sftp.listdir())

    # 2 Test deleting a non existing directory
    #    return error test
    print('TEST 2: Directory does not exists')
    usage = "Error: no such file or directory contains content at " + sftp.pwd + "/" + "Test12345"
    test(del_no_existing_file(sftp, "Test12345"), usage())

    # 3 Test deleting a existing directory with content
    #    return error test
    #    We do not want to delete directory with content.  not supported by pysftp
    print('TEST 3: Directory has content, unable to delete')
    usage = "Error: no such file or directory contains content at " + sftp.pwd + "/" + "Test123456"
    test(content_dir(sftp, "Test123456"), usage())





    sftp.close()

    print("End Test")
if __name__ == "__main__":
    main()


