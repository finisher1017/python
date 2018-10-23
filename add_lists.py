list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
count = 0
totals = []

for i in list1:
	result = list1[count] * list2[count]
	totals.append(result)
	count += 1

print(totals)