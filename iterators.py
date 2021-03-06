# A string is iterable because you can go through each letter that composes the string. It's not an iterator. Running iter("string") returns an iterator. The iterator will call next() on the iterator until it has completely cycled through. 

# when the iterator is exhausted and there is nothing more that comes from next(), Python throws a StopIterator error. 

# creating our own for loop
# this is meant to show what really happens when you write a for loop
def my_for(iterable, function):
	iterator = iter(iterable)
	while True:
		try:
			i = next(iterator)
		except StopIteration:
			print("End of iterator")
			break
		else:
			function(i)

def square(x):
	print(x*x)
		
my_for("hello", print)
my_for([1, 2, 3, 4, 5], square)


# writing a custom iterator
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	# this needs to return an iterator
	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration

for x in Counter(0, 10):
	print(x)

