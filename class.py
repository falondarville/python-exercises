# defining a class
# class names should be singular and written in uppercase camelcase
# the arguments and variable names don't have to be the same
# self refers to the current class instance
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

# make an instance of the class
user1 = User("Joe", "Smith", 123)
user2 = User("Blanca", "Roberts", 657)

print(user1.first, user1.last)
print(user2.first, user2.last)
