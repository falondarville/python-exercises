# for error handling in programs, it is good practice to use "try except" because it won't break the entirety of your code. 

# if we didn't use "if except", the message 'This still prints' would not indeed print

try:
	foobar
except NameError as err:
	print(err)
print("This still prints.")


# this is a more comprehensive error handling process and runs while the input is not a number. The finally will still run after the break. 
while True:
	try:
		print("Please enter a number.")
		num = int(input())
	except ValueError:
		print("That's not a number.")
	else: 
		# else runs when except does not
		print("You entered a number!")
		break
	finally:
		# this runs regardless
		print("Runs regardless.")

# another example using division
def divide(a, b):
	try:
		return a/b
	except ZeroDivisionError:
		print("Numbers are not divisible by zero.")
	except TypeError as:
		print("a and b must be ints or floats")
		print(err)

# using pdb (Python debugger) to set breakpoints
# this is not something that you keep in your code. It stays until you no longer need it. 
import pdb; pdb.set_trace()

first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# common pdb commands
# l for list, this will show you a map of the program with the breakpoint
# n for next line, this will move the debugger breakpoint to the next line
# p for print, use before the name of a variable to print that variable with its value
# c for continue, this will also have you exit debugging mode
# a to print all of the variables with their values


