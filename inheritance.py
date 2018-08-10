# inheritance is taking the properties from a base or parent class and defining a new class
# to use inheritance in Python, pass the parent class as an argument to the child class.
class Animal:
	cool = True

	def make_sound(self, sound):
		print(f"This animal says {sound}")

class Cat(Animal):
	pass

blue = Cat()
blue.make_sound("meow")
# the Cat class has access to the variables and methods in the parent class
print(blue.cool)

# when checking if blue is an instance of both the Animal and Cat class, we get True
print(isinstance(blue, Cat))