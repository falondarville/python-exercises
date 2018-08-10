class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	# def get_age(self):
	# 	return self._age

	# def set_age(self, new_age):
	# 	if age >= 0:
	# 		self._age = new_age
	# 	else:
	# 		self._age = 0

	# we use these two methods together to manipulate the age of the instance of the class, via a private variable called _age. 
	# when calling this method, you do not need parentheses. Use this to get the age.
	@property
	def age(self):
		return self._age

	# we use this setter function to prevent issues with the input that we can receive. For example, this method prevents the user from setting age to a negative number. This method takes the value that will replace the old age. 
	@age.setter
	# note that the second argument should be another value, and this variable name should be used when contructing the logic to determine the validity of the age
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("Age can't be negative")

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

# here we create an instance of the class Human
jane = Human("Jane", "Goodall", 45)
# this return whatever is in the property method, called age in our case
print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)
