class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color
	def show_info(self):
		print("Last name: "+self.last_name)
		print("Eye color: "+self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, num_of_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.num_of_toys = num_of_toys
	def show_info(self):
                print("Last name: "+self.last_name)
                print("Eye color: "+self.eye_color)
		print("Numbers of toys: "+str(self.num_of_toys))

billy_cyrus = Parent("Cyrus","Blue")
#print(billy_cyrus.last_name)
billy_cyrus.show_info()
#print(billy_cyrus.num_of_toys) Error, no attribute of num_of_toys
miley_cyrus = Child("Cyrus", "Blue", 5)
#print(miley_cyrus.num_of_toys)
miley_cyrus.show_info()
