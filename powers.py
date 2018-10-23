number = int(input("Enter a number: "))
power_of = int(input("To the power of: "))
tot = number
count = 0


while count < power_of - 1:
	calc = tot * number
	tot = calc
	count += 1	

print(tot)