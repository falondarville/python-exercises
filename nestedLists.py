# accessing nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# access the outer list, and then the inner list
nested_list[0][1] #2

nested_list[1][-1] #6

# iterating through nested lists
# prints all numbers 
# if you don't nest, you will print the three lists, not nine numbers
for i in nested_list:
	for val in i:
		print(val)

# nested list comprehension
[[print(val) for val in l] for l in nested_list]

# generate nested lists
board = [[num for num in range(1, 4) for val in range(1,4)]

# gives us [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# list comprehension and conditional logic
[['X' if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]

# gives us [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]

[["*" for x in range(1, 4)] for i in range(1, 4)]