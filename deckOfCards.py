from random import shuffle

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	# this is what will appear when you print the name of the instance of the class. In the example below, the instance is called "card" (lowercase) and displays the return value of the __repr__ method.
	def __repr__(self):
		return f"{self.value} of {self.suit}"

# card = Card("A", "hearts")
# print(card)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards."

	def count(self):
		return len(self.cards)

	# this is an internal method. It will take off a specified number of cards from the deck.
	def _deal(self, num):
		count = self.count()
		# find whether the number of cards in a deck or the number you want to remove is lower. This will prevent there being negative numbers. 
		actual = min([count, num])
		if count == 0:
			raise ValueError("All cards have been dealt.")
		# this is so that we are taking cards off the end of the deck
		cards = self.cards[-actual:]
		# we set self.cards to the beginning of the list
		self.cards = self.cards[:-actual]
		return cards

	def deal_card(self):
		# add the 0 position at the end so that you return a value and not a list
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)
		# even though we don't need to return self here, it's conventional that you do in case you need to store the value. 
		return self

d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(5)
print(hand)
