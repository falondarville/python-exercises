# Polymorphism is an object that takes on many forms. 

# There are two practical applications of polymorphism. One is when the same class method works in a similar way for different classes. The second is when the same operation works for different kinds of objects. 

# The classes that are inheriting from a parent class with the same method will run the method specified in the child class. 

# In the following, Animal is the parent class, from which Dog inherits its variables and methods. However, since the Dog class has a method with the same name, when we call Dog, the result will be the return statement defined in the Dog class and not the Animal class. This process is called method overriding. 
class Animal():
	def speak(self):
		raise NotImplementedError("Subclass needs to implement this method.")

class Dog(Animal):
	def speak(self):
		return "woof"