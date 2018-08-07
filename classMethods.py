# class methods are not very common. Instance methods are used a lot more. Class methods are not concerned with instances, but with the class itself. 
class User:

	active_users = 0

	# these normally go at the bottom of the class
	# note that to define a class method, you'll be explicit about it. With instance methods, you do not have to define them with the @ symbol because they are the default type of method.
	@classmethod
	def display_active_users(cls):
		return f"There are {cls.active_users} active users."

	# this class method takes a string parament of data seperated values, splits the data into three parts, and then creates an instance of the User class from that data
	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(',')
		return cls(first, last, int(age))

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

# instances of the class User
user1 = User("Joe", "Smith", 123)
user2 = User("Blanca", "Roberts", 657)

print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom.full_name())





