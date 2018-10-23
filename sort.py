def sort(a, b, arr):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

arr = [1,2,3,4,5,6]

a = int(input("First number: "))
b = int(input("Second number: "))
sort(a, b, arr)
print(arr)


