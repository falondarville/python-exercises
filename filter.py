# Filters out items based on a condition. You will be handing a lambda function to the filter function.

# The following takes a list and processes the list items through the lambda function, returning just the even numbers.
l = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

# The following checks the first letter in the names from the list, and returns names beginning with the letter f
# The premise of these is that it checks if the condition is true or false. Those conditions that are true are added to the a_names list. 
names = ["Frankfurt", "Fiona", "Flavor Flav", "Ralph"]
a_names = list(filter(lambda x: x[0]=="F", names))
print(a_names)

# Combine map and filter. In this scenario, we are going to map through items in the list, and then after that filter those down by the condition. 

# I created an exercise in which we will have a name and a grade. Those with at least 70 points will pass and gain a congratulations print-out. 
grades = [{"name": "Falon", "grade": 70}, {"name": "Marie", "grade": 45}, {"name": "JJ", "grade": 90}]

passing_grades = list(map(lambda x: x["name"],filter(lambda grade: grade["grade"] >= 70, grades)))

print(passing_grades)