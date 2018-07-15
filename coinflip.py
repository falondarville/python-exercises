from random import random

def flip_coin():
	rand_num = random()
	if rand_num > 0.5:
		return 'Heads'
	else:
		return 'Tails'

print(flip_coin())

# a shorter way to write the previous
def flip_coin_revamp():
	if random() > 0.5:
		return 'Heads'
	else:
		return 'Tails'

print(flip_coin_revamp())