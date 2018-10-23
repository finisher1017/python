# User picks 6 numbers
# Lottery calculates 6 random numbers (between 1 and 20)
# The we match the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched

#user_set = set()
#lottery_numbers = set()
import random

def menu():
	up = user_picks()
	lot = lottery()
	matches = up.intersection(lot)
	print(matches)

def user_picks():
	user_input = input("Enter six nuamber: ")
	user_split = user_input.split(",")
	user_set = {int(number) for number in user_split}
	return user_set

def lottery():
	lottery_numbers = set()

	while len(lottery_numbers) < 6:
		lottery_numbers.add(random.randint(1, 21))
	return lottery_numbers



menu()

 