#import required modules
import os


def rename_local_file(before,after):
	'''
	Method to rename a file in current directory.
	'''

	#Path is set to current working directory
	path='.'

	# Check if file is present on the current path
	if os.path.isfile(before):
		# Rename file name from rename.txt to renamed.txt
		os.rename(before,after)
	# Else display a user-friendly message to retry with the valid file name
	else:
		print("Sorry! File: " + before +" doesn't exist.")
		print("Please check the file name and try again later")
	