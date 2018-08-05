# defining a class
# class names should be singular and written in uppercase camelcase
# the arguments and variable names don't have to be the same
# self refers to the current class instance
# methods and variables beginning with a single underscore should be respected as private, and this is understood as a convention among developers. However, these methods and variables are not actually private, since Python doesn't have this capability. 
# variables and methods starting with two underscores are not conventional and will not run. Behind the scenes, Python is name mangling these variables and methods, so they are not accessible by the name you gave them. Instead they will look like: _className__variable/methodName
# don't define your own dunder variables __example__
class User:
	# define a class variable
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		# each time an instance of User is created, add one to active_users
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th birthday, {self.first}"

# make instances of the class
user1 = User("Joe", "Smith", 123)
user2 = User("Blanca", "Roberts", 657)

# print(user1.first, user1.last)
# print(user2.first, user2.last)
print(user1.full_name())
print(user1.initials())
print(user1.likes("candy"))
print(user1.is_senior())
print(user1.birthday())

# when accessing a class variable, identify the class name first
print(User.active_users)

print(user2.logout())

