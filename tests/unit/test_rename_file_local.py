import os
import pytest
import imp
import paramiko
import contextlib
from actions import rename_files_local as rename


def test_local_file_rename():
	'''
		Standard output of files is redirected and stored in stdout_string
		and checked if README.md file is listed while listing local files and
		directories
	'''
	# Original file name
	file_test='rename.txt'

	# New renamed file name
	renamed_file='renamed.txt'

	# List file and directories in cs410agile project folder
	path='.'

	# Check to handle FileNotFound Exception
	# Create a file to rename, if it doesn't exist
	if not os.path.isfile(file_test):
		open(file_test, 'a').close()
	# Call rename action to reanme filr from file_test to renamed_file
	rename.rename_local_file(file_test,renamed_file)

	# Assert true if renamed_file is present on file path
	assert os.path.isfile(renamed_file)