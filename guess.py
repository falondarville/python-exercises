import random

random_number = random.randint(1, 10)

# if the player guesses correctly, tell them they won
# otherwise, tell them if they are too high or too low

user_number = int(input("Please guess a number "))

while random_number != user_number:
	if random_number < user_number:
		print("You guessed too high!")
		user_number = int(input("Please guess a number "))
	else:
		print("You guessed too low!")
		user_number = int(input("Please guess a number "))
print("You won!")
user_input = input("Would you like to play again? Enter y or n: ")
if user_input == "y":
	user_number = int(input("Please guess a number "))