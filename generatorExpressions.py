# generator expressions
def nums():
	for num in range(1, 10):
		yield num

g = nums()
next(g)

# the above can also be written as
# this returns a generator object
h = (num for num in range(1, 10))

# if you wrap the above in [] instead of (), you get a list of all of the numbers in range returned


