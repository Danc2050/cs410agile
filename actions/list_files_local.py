#import required modules
import os

'''
	Method to display the files in current directory.
'''
def display_local_files():
	#Path is set to current working directory
	path='.'


	for file in os.listdir(path):
		if not file.startswith('.'):
			print(file)

	