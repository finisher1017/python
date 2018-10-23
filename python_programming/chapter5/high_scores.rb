scores = []
choice = ""

while choice != "0"
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
	print("Enter choice: ")
	choice = gets().chomp()

	#exit
	if choice == "0"
		print("Good Bye!")
		break
	elsif choice == "1"
		print("High Scores\n")
		for score in scores
			print(score, "\n")
		end
	elsif choice == "2"
		print("Enter score: ")
		score = gets().chomp().to_i
		scores << score
	elsif choice == "3"
		print("Remove score: ")
		score = gets().chomp().to_i
		if scores.include?(score)
			scores.delete(score)
		else
			print("#{score} not in list\n")
		end
	elsif choice == "4"
		scores = scores.sort().reverse()
		print("Scores sorted.\n")
		print(scores)	
	end
end
