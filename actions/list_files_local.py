import os

def display_local_files():
	path='.'
	files = open('output_file.txt','w+')
	for file in os.listdir(path):
		if not file.startswith('.'):
			print(file)
			files.write(file)
			files.write("\n")

	files.close() 
