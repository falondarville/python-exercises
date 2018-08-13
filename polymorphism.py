# There are two practical applications of polymorphism. One is when the same class method works in a similar way for different classes. The second is when the same operation works for different kinds of objects. 

# The classes that are inheriting from a parent class with the same method will run the method specified in the child class. 
class Animal():
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method.")

class Dog(Animal):
	def speak(self):
		return "woof"