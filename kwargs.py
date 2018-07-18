# *args is an operator we can hand to functions. It gathers the arguments in a tuple. 
def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total

print(sum_all_nums(1, 4, 5))

# LIST AND TUPLE UNPACKING
# what happens if you have a list of data, like the following, and you want to hand it to the function, thereby "unpacking" it (breaking the list into individual elements)?
nums = [1, 2, 3, 4, 5, 6]
# if you pass the name of the list variable in directly, you get an error for operand type.
# result is this: ([1, 2, 3, 4, 5, 6],)
# Note the trailing comma, because you've handed one item to a tuple.
# adding the asterick works with tuples and lists. This will break the tuple or list into individual items that can then be run through the for loop, as defined above.
sum_all_nums(*nums)

# **kwargs is another operator that we can hand to functions. It gathers the keyword arguments as a dictionary. 
def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(Falon="black", Martha="teal", Marie="magenta")

# checking if a value and a value appears in kwargs (*args can also be checked). Hand the function a key value pair. 
def greeting(**kwargs):
	if "Falon" in kwargs and kwargs["Falon"] == "special":
		return "You get a special greeting"
	elif "Falon" in kwargs:
		return f"{kwargs['David']} Falon!"
	return "Not sure who this is..."

# note that the code is only looking for "Falon", so it doesn't matter if I pass more than one key value pair in these. 
print(greeting(Falon="special"))
print(greeting(Bob="hello"))
