# Rock Paper Scissors Game
# Goal: Create a game of RPS that allows player to continue playing if desired.
# Last Updated: 10/03/2016
#
# Changelog:
# Version 1.0
#	- 10/03/16: Initial Release.

# Imports
import random

# Start the game and ask the user if they want to play:
print('________ROCK PAPER SCISSORS________\n\n')

print('Would you like to play? (y/n)')
play = raw_input('> ')

# Setup variables
playerScore = 0
compScore = 0

options = ['rock','paper','scissors']

# Loop through gameplay
while play == 'y':

	# Print score:
	print('\nPlayer: %d | Computer: %d \n') % (playerScore, compScore)

	# Ask player to make their choice:
	playerChoice = raw_input('Make your choice (r,p,s): ')


	# Have computer make a choice:
	compChoice = random.choice(options)

	# Show computer choice, determine the winner
	print('The computer threw %s!') % compChoice


	if playerChoice == compChoice[0]:						# Tie Case
		print('Tie!\n')
	elif playerChoice == 'r':
		if compChoice[0] == 's':							# Player r>s
			print('Rock breaks scissors. You win!\n')
			playerScore += 1
		else:												# Computer p>r
			print('Paper covers rock. You lose.\n')
			compScore += 1
	elif playerChoice == 'p':
		if compChoice[0] == 'r':							# Player p>r
			print('Paper covers rock. You win!\n')
			playerScore += 1
		else:												# Computer s>p
			print('Scissors cut paper. You lose.\n')
			compScore += 1
	else:
		if compChoice[0] == 'p':							# Player s>p
			print('Scissors cut paper. You win!\n')
			playerScore += 1
		else:												# Computer r>s
			print('Rock breaks scissors. You lose.\n')
			compScore += 1

	print('Play again (y/n)?')
	play = raw_input('> ')


print('Final Scores - Player: %d | Computer: %d \n') % (playerScore, compScore)
print('Have a nice day!')