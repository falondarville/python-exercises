# when you create a class, Python sets an MRO, or Method Resolution Order. This is the order that Python is going to look for methods of a class. This is useful to think about in the scenario that you have two methods with the same name, under two different classes. 

# to get the MRO of a class, use help(className)

# example of a class that inherits from two classes
class Child(Mother, Father):
	pass
