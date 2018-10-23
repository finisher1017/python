import random

start = int(input("Enter the starting number: "))
finish = int(input("Enter the ending number: "))
count = int(input("Enter the count by: "))
num_range = range(start, finish, count)
for i in num_range:
	print(i)


