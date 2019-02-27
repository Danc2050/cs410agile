#import required modules
import pysftp

IO_ERROR_MESSAGE = "Unable to rename file, IO Error is raised."
ERROR_MESSAGE = "Couldn't rename file! Please check the file name and try again later."

def rename_remote_file(sftp: pysftp.Connection, before:str, after:str):
	'''
	Method to rename a file in current directory.
	'''

	#Path is set to current working directory
	path='.'
	# Check if file is present on the current path
	try:
		# Rename file name from rename.txt to renamed.txt
		sftp.rename(before,after)
		return True
	except IOError:
		print(IO_ERROR_MESSAGE)
	except FileNotFoundError:
		print(ERROR_MESSAGE)
		return False
	except OSError:
		print("You might not have permissions to rename this file.")
		print("Please check permissions and try again.")
		return False
