import random

random_number = random.randint(1, 10)

# if the player guesses correctly, tell them they won
# otherwise, tell them if they are too high or too low

user_number = input("Please guess a number ")

if random_number == user_number:
	print("You won!")
	user_input = input("Would you like to play again? Enter y or n")
	if user_input == y:
		user_number = input("Please guess a number ")
	else:
		break
elif random_number < user_number:
	print("You guessed too high!")
else:
	print("You guessed too low!")