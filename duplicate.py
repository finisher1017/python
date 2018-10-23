str = "nintendo"
arr = []

for i in str:
	if i in arr:
		print(i)
		break
	else:
		arr.append(i)
