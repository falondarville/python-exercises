# generators are iterators and can be made using generator functions that use the yield keyword
# in typical functions, you will return and you can do this once. In a generator function, you will yield, and you can do this multiple times. 
def count_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1

# creates a generator object that can be iterated through
counter = count_to(8)

# cycle through iterator
for num in counter:
	print(num)