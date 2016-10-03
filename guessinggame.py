# Number Guessing Game

import random

# Generate correct answer
number = random.randint(1,100)
print number
guess = 0

# Guess until correct
while guess != number:
	print number
	guess = int(raw_input('Input your guess (1-100): '))

	if guess > number:
		print('Too high! Try again.\n')
	elif guess < number:
		print('Too low! Try again.\n')

print('You guessed right!')