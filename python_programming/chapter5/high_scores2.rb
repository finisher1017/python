scores = []

choice = ""
while choice != "0"


	print(
	"""

	High Scores 2.0

	0 - Quit
	1 - List Scores
	2 - Add a score
	"""

	)

	print("Choice: ")
	choice = gets().chomp()
	#exit
	if choice == "0"
		print("Good-bye!\n")
	#list high-scores
	elsif choice == "1"
		print("High Scores\n")
		print("NAME\tSCORE")
		for entry in scores
			score, name = entry
			print("\n#{name} \t #{score}")
		end
	elsif choice == "2"
		print("Enter name: ")
		name = gets().chomp()
		print("Enter score: ")
		score = gets().chomp()
		entry = score, name
		scores << entry
		scores = scores.sort().reverse()
	else
		print("Invalid Entry\n")
	end
end