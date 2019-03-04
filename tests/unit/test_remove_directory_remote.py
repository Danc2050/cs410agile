# Import required libraries
import pysftp
import pytest
import paramiko
from actions import remove_directory_on_remote as rmdirectory


def test_remote_remove_directory(sftp):
	"""
		Test to check if the valid directory is deleted on remote server.
		This test first create a directory on remote server, and then delete it successfully
	"""

	# Directory name to create
	dir_test = 'directory_test'

	# Call mkdir function to create directory on remote server
	sftp.makedirs(dir_test)

	#Delete it
	rmdirectory.remove_dir_remote(sftp, dir_test)

	# Check if dir_test is deleted on remote server
	assert sftp.isdir(dir_test) is False


def test_remote_remove_directory_invalid(sftp,capsys):
	"""
		Test to check if pysftp.rmdir can handle invalid directory names and 
		empty string directory names.
	"""
	cases = [
		"http://www.google.com",
		"",
		".",
		"/test_create_directory_invalid"
	]
	for dir_test in cases:
		# Each case should fail and print an error message.
		assert rmdirectory.remove_dir_remote(sftp, dir_test) is False
		assert rmdirectory.ERROR_PREFACE in capsys.readouterr().out


def test_remote_remove_directory_existing(sftp,capsys):
	"""
		Test to check if pysftp.rmdir can handle special cases like removing directory 
		having file inside it.
	"""
	file_test = "file_test.txt"
	dir_test = "directory_test"

	# Create a directory and a file inside directory to delele on the remote server
	sftp.makedirs(dir_test)
	sftp.open(dir_test +'/' + file_test, mode='a+').close()

	# Test trying to delete a directory that contains a file within it
	assert rmdirectory.remove_dir_remote(sftp, dir_test) is False
	assert rmdirectory.ERROR_PREFACE in capsys.readouterr().out

	# Clean-up (remove newly created file and directory from remote server)
	sftp.remove(dir_test +'/' + file_test)
	sftp.rmdir(dir_test)
