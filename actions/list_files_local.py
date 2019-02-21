#import required modules
import os

def display_local_files():
	"""
        	Method to display the files in current directory.
	"""
	
	#Path is set to current working directory
	path='.'


	for file in os.listdir(path):
		if not file.startswith('.'):
			print(file)


	
