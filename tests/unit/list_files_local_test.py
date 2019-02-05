import os
import pytest
import imp

#import actions directory module to list files
display = imp.load_source('list_files_local',"../../actions/list_files_local.py")

'''
Tests to compare the output of python program to list files with
the output of the ls linux command 
'''

def test_local_file_listing():
	# Path is assigned as the path of current working directory
	path='.'

	cmd = 'ls > test_output_file.txt'

	#Execute the linux command to list the files and write it to a text file
	os.system(cmd)


	#Call python function to display list of files in current directory
	display.display_local_files()   

	#Compare results
	assert len(open('test_output_file.txt').readlines()) == len(open('output_file.txt').readlines())

def test_difference_in_output():
    #Read the contents of file to Set datastructure
	output = set((file.strip() for file in open("output_file.txt")))
	output_test = set((file.strip() for file in open("test_output_file.txt")))

	# Print the file difference between test output and main program's output
	with open('difference.txt', 'w') as diff:
		for f in output:
			if f not in output_test:
				diff.write(f)
		for f in output_test:
			if f not in output:
				diff.write(f)

	# If difference file is empty than the results are identical and test should pass
	assert len(open('difference.txt').readlines()) == 0

# Execute tests
test_local_file_listing()
test_difference_in_output()
