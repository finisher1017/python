scores = []
choice = None

while choice != "0":
	print(
		"""
		High Scores

		0 - Exit
		1 - Show Scores
		2 - Add a Score
		3 - Delete a Score
		4 - Sort Scores
		"""

		)
	#exit
	choice = input("Choice: ")
	if choice == "0":
		print("Good-bye.")
	# list high-scores table
	elif choice == "1":
		print("High Scores")
		for score in scores:
			print(score)
	# add a score
	elif choice == "2":
		score = int(input("Enter score: "))
		scores.append(score)
	# remove a score
	elif choice == "3":
		score = int(input("Remove score: "))
		if score in scores:
			scores.remove(score)
		else:
			print(score, "not in list.")
	# sort scores
	elif choice == "4":
		scores.sort(reverse=True)
	# invalid choice
	else:
		print("Invalid choice.")


