# Import required libraries
import pysftp
import pytest
import paramiko
from actions import create_directory_on_remote as mkdirectory


def test_remote_create_directory(sftp):
	"""
		Test to check if the file is renamed by rename_remote_file action.
		This test first create a file on remote server, rename it and then remove 
		it once the test assertion is complete.
	"""

	# Directory name to create
	#dir_test='dir_test'
	dir_test='directory_test'

	# Call mkdir function to create directory on remote server
	mkdirectory.create_dir_remote(sftp, dir_test)

	# Check if dir_test is created on remote server
	assert sftp.isdir(dir_test) is True

	# Clean-up (remove newly created directory from remote server)
	sftp.rmdir(dir_test)

def test_remote_create_directory_invalid(sftp,capsys):
	"""
		Test to check if pysftp.mkdir can handle invalid directory names and 
		empty string directory names.
	"""
	cases = ["http://www.google.com", "", ".", "/test_create_directory_invalid"]
	for dir_test in cases:
		# return type of pysftp rename function is None
		assert mkdirectory.create_dir_remote(sftp, dir_test) is False
		# cases should raise OSError
		assert mkdirectory.ERROR_PREFACE in capsys.readouterr().out

def test_remote_create_directory_existing(sftp,capsys):
	"""
		Test to check if pysftp.mkdir can handle special cases like file name 
		or directory with the same name exists already.
	"""
	file_test = "file_test.txt"
	dir_test = "directory_test"

	# Create a file and directory to rename on the remote server
	sftp.open(file_test, mode='a+').close()
	sftp.mkdir(dir_test, mode=755)
	
	# return type of pysftp rename function is boolean
	assert mkdirectory.create_dir_remote(sftp, file_test) is False
	# cases should raise OSError as file with same name already exists
	assert mkdirectory.ERROR_PREFACE in capsys.readouterr().out

	# return type of pysftp rename function is boolean
	assert mkdirectory.create_dir_remote(sftp, dir_test) is False
	# cases should raise OSError as directory with same name already exists
	assert mkdirectory.ERROR_PREFACE in capsys.readouterr().out

	# Clean-up (remove newly crteated file and directory from remote server)
	sftp.remove(file_test)
	sftp.rmdir(dir_test)




	
