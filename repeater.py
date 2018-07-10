print("How many times do I have to tell you?")
num = input()
# convert the input into an integer
num = int(num)

# pick an iterator then put num in a range, and it will take your num as the max number, starting at 0
for i in range(num):
	print("Clean your room!")