#import required modules
import pysftp

ERROR_MESSAGE = "Couldn't rename file! Please check the file name and try again later."

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
    	print(ERROR_PREFACE, e.strerror)
		return False
