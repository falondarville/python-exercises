class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"This animal says {sound}")

class Cat(Animal):
	def __init__(self, name, breed, toy):
		# super refers to the parent class Animal
		super().__init__(name, species="cat")
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

buddy = Cat("Buddy", "domestic shorthair", "feather wand")

print(buddy)
buddy.play()