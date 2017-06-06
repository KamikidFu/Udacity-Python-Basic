import os 

def rename_files():
	saved_path = os.getcwd()
	#1 get file names from a folder
	file_list = os.listdir("/home/vagrant/udacity/pyBase/pics")
	#print(file_list)
	#2 for each file, rename it
	os.chdir("/home/vagrant/udacity/pyBase/pics")
	for file_name in file_list:
		os.rename(file_name,file_name.translate(Node, "0123456789"))
	os.chdir(saved_path)

rename_files()
