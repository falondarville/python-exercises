class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def __repr__(self):
		return f"Human named {self.first} {self.last}"

	# If you want to get the length of your Human instance, you need to add the method __len__ here
	# This is example is a bit odd. So the len here means print the age. len of life?
	def __len__(self):
		return self.age

	# hand argument like so: j + k
	def __add__(self, other):
		# check that the argument handed to this method is an instance of the class Human. Otherwise don't run the method. 
		if isinstance(other, Human):
			return Human(first="Newborn", last=self.last, age=0)
		# normally you would raise a typeerror here
		return "You can't add that."

	# cloning humans using multiplication
	def __mul__(self, other):
		# check that the second argument passing is an integer
		if isinstance(other, int):
			return [self for i in range(other)]
		# normally you would raise a typeerror here
		return "You are cloning humans"

j = Human("Jorgen", "Jergens", 89)
k = Human("Kervel", "Kringle", 67)
print(j)
print(len(j))

print(j + k)
print(j * 2)