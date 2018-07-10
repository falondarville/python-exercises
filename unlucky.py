# Loop through 1 and 20, inclusive
# for 4 and 13, print x is unlucky
# for even numbers, print x is even
# for odd numbers, print x is odd

for i in range(1, 21):
	if i == 4 or i == 13:
		print(f"{i} is unlucky")
	elif i % 2 == 0:
		print(f"{i} is even")
	else:
		print(f"{i} is odd")