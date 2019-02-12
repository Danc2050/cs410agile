import os
import pytest
import imp
import paramiko
import contextlib
from io import StringIO
from actions import list_files_local as display

'''
	Test to check if the specific file is displayed while listing the 
	files and directories on local machine.
'''
def test_local_file_listing():
	'''
		Standard output of files is redirected and stored in stdout_string
		and checked if README.md file is listed while listing local files and
		directories
	'''
	stdout_string = StringIO()

	# README.md file should always be present in cs410agile project folder
	filename="README.md"

	# app directory should always be present in cs410agile project folder
	dirname="app"
	
	# List file and directories in cs410agile project folder
	path='.'

	# Redirect standard output and store it as a list
	with contextlib.redirect_stdout(stdout_string):
		display.display_local_files()

	output = stdout_string.getvalue().strip()

	# Checks if README.md is in output list
	assert filename in output and dirname in output
