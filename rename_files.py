import os

def rename_files():
	#1 get file names from a folder
	file_list = os.listdir("/home/vagrant/udacity/pyBase/pics")
	print(file_list)
	#2 for each file, rename it

rename_files()
