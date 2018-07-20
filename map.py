# a map is a function that takes two arguments: a function and an iterable. Map runs the lambda function for each value in the iterable and returns a map object, which is to be converted into another data structure. 
nums = [2, 4, 6, 8, 10]

doubles = map(lambda x: x*2, nums)
print(doubles)
# returns <map object at 0x10e1e5da0>

# with the above returned map object, iterate through:
for num in doubles:
	print(num)

# alternatively, you can convert the variable doubles to a list

# map items can only be iterated once, it you called the doubles function a second time on the same list, the list converted variable doubles would print as empty. 

# typically, you would convert the result of the map function on the same line to a list like so:
# doubles = list(map(lambda x: x*2, nums))

people = ["Falon", "Marie", "Sally", "Martha"]

persons = list(map(lambda name: name.upper(), people))

print(persons)

# example of lambda used on dictionary
coffee = [
	{'type': 'light roast', 'taste': 'airy, aromatic'},
	{'type': 'medium roast', 'taste': 'smooth, rich'},
	{'type': 'dark roast', 'taste': 'chocolatey, velvety'}
]

coffee_taste = list(map(lambda x: x['taste'], coffee))

print(coffee_taste)

# You can also pass the name of a function directly into map without using a lambda. 
def double(x): return x*2

doubled = list(map(double, nums))

print(doubled)

# The benefit of using a lambda is that you're writing all of the code on a single line. 