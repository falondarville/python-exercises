class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	# this is what will appear when you print the name of the instance of the class. In the example below, the instance is called "card" (lowercase) and displays the return value of the __repr__ method.
	def __repr__(self):
		return f"{self.value} of {self.suit}"

card = Card("A", "hearts")
print(card)

# class Deck:
# 	def __init__(self):