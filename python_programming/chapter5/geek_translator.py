geek = {"404": "Clueless. From the web error 404, meaning page not found.",
		"Googling": "searching the internet.",
		"Keyboard Plaque": "the collection of debri found in computer keyboards.",
		"Link Rot": "the process by which web page links become obsolete.",
		"Uninstalled": "being fired.",
		1: 100}

choice = None

while choice != "0":
	

	print(
	"""

	Geek Translator

	0 - Quit
	1 - Look Up Term
	2 - Add Term
	3 - Redefine Term
	4 - Delete Term
	"""

	)
	
	choice = input("Choice: ")
	print()

	#exit
	if choice == "0":
		print("Good-bye!")
	#get a definition
	elif choice == "1":
		term = input("Enter key: ")
		if term in geek:
			definition = geek[term]
			print(definition)
		else:
			print("Key not in dictionary")
	# add a term-definition pair
	elif choice == "2":
		term = input("Add term: ")
		if term not in geek:
			definition = input("\nAdd definition: ")
			geek[term] = definition
			print("\n", term, "has been added.")
		else:
			print("Term already exists.")
	# redefining an existing term
	elif choice == "3":
		term = input("Enter term to redefine: ")
		if term in geek:
			definition = input("Enter new definition: ")
			geek[term] = definition
			print(term, "has been redefined\n")
		else:
			print("Term not in dictionary.")
	# delete term
	elif choice == "4":
		term = input("Delete term: ")
		if term in geek:
			del geek[term]
			print(term, "deleted.")
		else:
			print("\nTerm not in dictionary.")
	else:
		print("Invalid choice.")
