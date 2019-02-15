#import required modules
import os

'''
	Method to re=name a file in current directory.
'''
def rename_local_file(before,after):
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
	

rename_local_file('rename.txt','renamed.txt')