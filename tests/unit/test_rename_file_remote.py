# Import required libraries
import pysftp
import pytest
import paramiko
from actions import rename_file_remote as rename_display


def test_remote_file_rename(sftp):
	"""
		Test to check if the file is renamed by rename_remote_file action.
		This test first create a file on remote server, rename it and then remove 
		it once the test assertion is complete.
	"""

	# Original file name
	file_test='rename.txt'

	# New renamed file name
	renamed_file='renamed.txt'

	# Create a file to rename on the remote server
	sftp.open(file_test, mode='a+')
	# Call rename action to rename file from file_test to renamed_file
	rename_display.rename_remote_file(sftp, file_test, renamed_file)

	# Check if file_test is renamed to renamed_file
	assert sftp.isfile(renamed_file) is True

	# Check if file_test is renamed 
	assert sftp.isfile(file_test) is False

	# Clean-up (remove renamed file)
	sftp.remove(renamed_file)
	

def test_remote_rename_file_names(sftp,capsys):
	"""
		Test to check if pysftp.rename can handle invalid filenames, empty string filename,
		file not present etc.
	"""
	cases = [
	    ("http://www.google.com", "after.txt"),
	    ("","after.txt"),
	    ("before.txt",""),
	    ("before.txt","http://www.google.com"),
	    ("before.txt","folder")
	]
	for before, after in cases:
		# return type of pysftp rename function is None
		assert rename_display.rename_remote_file(sftp, before, after) is None
		# cases should raise IO Error
		assert rename_display.IO_ERROR_MESSAGE in capsys.readouterr().out
