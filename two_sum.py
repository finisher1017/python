arr = [2, 7, 5, 11, 15]
target = 9

def twoSum(arr, target):
	seen = {}
	for i in range(len(arr)):
		print(arr[i])
		seen[arr[i]] = target - arr[i]
		if seen[arr[i]] in seen:
			print("True")
		else:
			print("False")
	print(seen)

twoSum(arr, target)