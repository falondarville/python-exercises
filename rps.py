from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score: {player_wins} Computer score: {computer_wins}")
	print("Enter your choice.")
	player = input().lower()
	if player == "quit" or input == "q":
		break
	print(f"You chose {player}.")

	randomNumber = randint(1,3)

	computer = None

	if randomNumber == 0:
		computer = "rock"
	elif randomNumber == 1:
		computer = "paper"
	else:
		computer = "scissors"

	print(f"The computer generated {computer}.")

	if player and computer:
		if (player == "rock" and computer == "paper") or (player == "scissors" and computer == "rock") or (player == "paper" and computer == "scissors"):
			print("The computer won!")
			computer_wins += 1
		elif player == computer:
			print("Tie!")
		else:
			print("You won!")
			player_wins += 1
if player_wins > computer_wins:
	print("Congrats, you won!")
elif player_wins == computer_wins:
	print("It's a tie!")
else:
	print("Oh no, the computer won!")
print(f"FINAL SCORE... Player: {player_wins} Computer: {computer_wins}")