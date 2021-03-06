# These are some examples of list comprehension

# prints [10, 20, 30, 40, 50]
print([num*10 for num in range(1,6)]) 

# prints if the value in the list is truthy or falsy
# prints [false, false, false]
print([bool(val) for val in [0, [], '']])

# the following takes a list of numbers and converts each number to a string
numbers = [1, 2, 3, 4, 5]

string_list = [str(num) for num in numbers]

print(string_list)

# list comprehension with conditional logic
numberList = [1, 2, 3, 4, 5, 6]

evens = [num for num in numberList if num % 2 == 0]

odds = [num for num in numberList if num % 2 != 0]

print(evens)
print(odds)

# the following is another way to write list comprehension
[num*2 if num % 2 == 0 else num/2 for num in numbers]

# check for values in common across two lists
answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]

# make items in list lowercase and reverse them
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

# print a string as a list, after taking out the vowels
answer3 = [char for char in "amazing" if char not in "aeiou"] 

