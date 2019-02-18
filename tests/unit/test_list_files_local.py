import os
import pytest
import imp
import paramiko
import contextlib
from actions import list_files_local as display


def test_local_file_listing(capsys):
	"""
	Test to check if the specific file is displayed while listing the 
	files and directories on local machine.
	"""
	
	# Display the local files; we'll test the output against known values.
	display.display_local_files()

	# Save the captured stdout output so we can check against it
	# multiple times.
	output = capsys.readouterr().out

	# List of files to search for. We'll use one file and one folder
	# that should definitely be there.
	files_to_find = ["README.md", "app"]

	# Check for each file in the output.
	for file in files_to_find:
		assert file in output