# since there are only two options, you don't need an else statement in the following
# if the condition is true, the rest of the code won't run, and that's why you don't need to add an else statement. The first return will exit the function
def is_odd_number(num):
	if num % 2 != 0:
		return True
	return False

print(is_odd_number(2))