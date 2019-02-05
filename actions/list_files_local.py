#import required modules
import os

'''
	Method to display the files in current directory.
'''
def display_local_files():
	#Path is set to current working directory
	path='.'

	# Create and open file to append the output files list to a text file
	files = open('output_file.txt','w+')

	# iterate through each entry and check if file name starts with '.'
	# If yes, then skip that entry and move on to the next.
	for file in os.listdir(path):
		if not file.startswith('.'):
			print(file)
			files.write(file)
			files.write("\n")

	# Close the output text file
	files.close() 
