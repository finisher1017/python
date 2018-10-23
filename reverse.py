#str = "string"

def reverse_string(str):
	rev_str = []

	for i in str:
		rev_str.insert(0, i)

	pal = "".join(rev_str)

	if pal == str:
		print("True")
	else:
		print("False")

reverse_string(input())