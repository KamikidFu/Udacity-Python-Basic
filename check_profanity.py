import urllib

def read_text(URL):
	quotes = open(URL)
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(key):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+ key)
	output = connection.read()
	print(output)
	connection.close()

read_text("/home/vagrant/udacity/pyBase/test_profanity.txt")
