scores = []

choice = None
while choice != "0":


	print(
	"""

	High Scores 2.0

	0 - Quit
	1 - List Scores
	2 - Add a score
	"""

	)

	choice = input("Choice: ")
	print()
	#exit
	if choice == "0":
		print("Good-bye!")
	#display high-score table
	elif choice == "1":
		print("High Scores\n")
		print("NAME\tSCORE")
		for entry in scores:
			score, name = entry
			print(name, "\t", score)
	#add score
	elif choice == "2":
		name = input("Enter name: ")
		score = int(input("Enter score: "))
		entry = (score, name)
		scores.append(entry)
		scores.sort(reverse=True)
		scores = scores[:5]
	#invalid entry
	else:
		print("Invalid Entry.")