import random as r
#nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
number = 51
begin = 1
end = 100



solved = False
while solved == False:
	num_list = []
	num_range = range(begin, end)
	pos = round(len(num_range) / 2)
	for i in num_range:
		num_list.append(i)
	guess = num_list[pos]
	print(guess)
	print(num_list)
	if guess == number:
		print("Correct!")
		solved == True
		break
	elif guess < number:
		print("Higher")
		begin = guess + 1
		continue
	elif guess > number:
		print("Lower")
		end = guess
		continue


