pairs = {"Jon" => "Chris", "Chris" => "Ed", "Mark" => "Chris", "Jordan" => "Mark", "Steven" => "David"}

choice = ""

while choice != "0"


	print(
	"""

		0 - Quit
		1 - Look Up Pair
		2 - Add Pair
		3 - Delete Pair

	"""

	)

 
	print("Choice: ")
	choice = gets().chomp()

	# exit
	if choice == "0"
		print("Good-bye!")
	# lookup a pair
	elsif choice == "1"
		print("Enter son: ")
		son = gets().chomp()
		if pairs.include?(son)
			print(pairs[son])
		else
			print("#{son} not in dictionary")
		end
	
	# add a pair
	elsif choice == "2"
		print("Enter son to add: ")
		son = gets().chomp()
		if pairs.include?(son)
			print("#{son} is already in the dictionary.")
		else
			print("Enter the father of the son: ")
			father = gets().chomp()
			pairs[son] = father

		end
		
	# delete a pair
	elsif choice == "3"
		print("Enter a son to delete: ")
		son = gets().chomp()
		if pairs.include?(son)
			pairs.delete(son)
			print("#{son} deleted")
			
		else
			print("#{son} is already in the dictionary.")
		end
				
	end
end