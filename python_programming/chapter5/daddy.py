pairs = {"Jon" : "Chris", "Chris" : "Ed", "Mark" : "Chris", "Jordan" : "Mark", "Steven" : "David"}

choice = None

while choice != "0":


	print(
	"""

		0 - Quit
		1 - Look Up Pair
		2 - Add Pair
		3 - Delete Pair

	"""

		)

	choice = input("Choice: ")
	# exit
	if choice == "0":
		print("Good-bye!")
	
	# look up pair
	if choice == "1":
		son = input("Enter the name of a son: ")
		if son in pairs:
			print(pairs[son])
		else:
			print(son, "is not in dictionary.")

	# add a pair
	if choice == "2":
		son = input("Enter the name of a son to add: ")
		if son not in pairs:
			father = input("Enter the name of the son's father: ")
			pairs[son] = father
		else:
			print(son, "already in dictionary.")

	# delete a pair
	if choice == "3":
		son = input("Enter name of son to delete: ")
		del pairs[son]
		print(son, "deleted.")

