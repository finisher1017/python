def number_of():
	total = 0
	count = int(input("Number of pushups: "))
	while count > 0:
		total += count
		count -= 1

	return total

print(number_of())

