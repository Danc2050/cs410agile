#import required modules
import pysftp

ERROR_PREFACE = "Error:"

def rename_remote_file(sftp: pysftp.Connection, before:str, after:str):
	'''
	Method to rename a file on remote server.
	'''

	#Path is set to current working directory
	path='.'
	
	try:
		# Rename file name from rename.txt to renamed.txt on remote server
		# If rename is unsuccessful, then None is returned
		sftp.rename(before,after)
		return True
	except OSError as e:
		if e.strerror is None:
			print(ERROR_PREFACE, "could not rename file or directory.")
		else:
			print(ERROR_PREFACE, e.strerror)
		return False


	