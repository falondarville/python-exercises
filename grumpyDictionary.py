# we don't need to add __init__ because we're only concerned with adding some new methods
class GrumpyDict(dict):

	# the portion with super actually prints the items inside of the dictionary.
	def __repr__(self):
		print("None of your business.")
		return super().__repr__()

	# this will automatically be called if you search for a key that is not present in the dictionary. 
	def __missing__(self, key):
		print(f"You want {key}? It's not here.")

	# this will automatically be called when you try to set a new item in the dictionary.
	def __setitem__(self, key, value):
		print("You want to change the dictionary?")
		print("fine.")
		# to actually update the dictionary, you need to add the following:
		super().__setitem__(key, value)

	# this method returns false even if the item exists in the dictionary
	def __contains__(self, item):
		print("I'm not going to bother looking.")
		return False

data = GrumpyDict({"first": "Buddy", "animal": "cat"})
print(data)
data["city"]
data["city"] = "Los Angeles"
print(data)
"city" in data