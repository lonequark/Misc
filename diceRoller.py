# DICE ROLLING SIMULATOR
# Simulates rolling X number of Y-sided dice and reports the results (for DnD, etc.)
# Last Updated: MM/DD/YEAR
#
# Changelog:
# Version 1.0
#	- MM/DD/YY: Initial Release.
#
#


# Imports
import random

def roll(num,sides):
	rolls = []
	for i in range(0, num):
		current = random.choice(range(1,sides+1))
		rolls.append(current)
	return rolls

# Prompt user to choose between character generation or regular:
gen = raw_input('Character generation? (y,n): ')


# For regular rolling:
if gen != 'y':
	repeat = 'y'
	while repeat == 'y':
		num = int(raw_input('Number of dice: '))
		sides = int(raw_input('Number of sides: '))

		rolls = roll(num,sides)

		print('\n%dd%d') % (num,sides)
		print('Rolls: [%s]') % ', '.join(map(str, rolls))
		print('Sum: %d \n') % sum(rolls)

		repeat = raw_input('Roll again? (y,n): ')

# For character generation:
else:
	num = 4
	sides = 6

	print('\n Roll 4d6 and drop the lowest for each set. \n\n')

	# Roll and print the results, then print the sum of the highest three. repeat 6 times
	for i in range(0,6):

		rolls = roll(num,sides)
		rolls.sort(reverse = True)

		print('[%s]') % ', '.join(map(str, rolls))

		print('Sum of best 3: %d \n') % sum(rolls[0:3])

print("\nEnd of rolling.")