# *args is an operator we can hand to functions. It gathers the arguments in a tuple. 
def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total

print(sum_all_nums(1, 4, 5))

# **kwargs is another operator that we can hand to functions. It gathers the keyword arguments as a dictionary. 
def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(Falon="black", Martha="teal", Marie="magenta")