geek = {"404" => "Clueless. From the web error 404, meaning page not found.",
		"Googling" => "searching the internet.",
		"Keyboard Plaque" => "the collection of debri found in computer keyboards.",
		"Link Rot" => "the process by which web page links become obsolete.",
		"Uninstalled" => "being fired.",
		1 => 100}

choice = ""

while choice != "0"
	

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

	print("Enter choice: ")
	choice = gets().chomp()

	#exit
	if choice == "0"
		print("Good-bye!\n")
	# look up term
	elsif choice == "1"
		print("Enter a term: ")
		term = gets().chomp()
	 	if geek.include?(term)
	 		print(geek[term] + "\n")
	 	else
	 		print("Term not in dictionary.")
	 	end
	# add term
	elsif choice == "2"
		print("Add term: ")
		term = gets().chomp()
		if geek.include?(term)
			print("Term already exists\n")
		else
			print("Add definition: ")
			definition = gets().chomp()
			geek[term] = definition
			print("#{term} added to dictionary\n")
		end 
	# redefine a teerm
	elsif choice == "3"
		print("Enter term to redefine: ")
		term = gets().chomp()
		if geek.include?(term)
			print("Enter new definition: ")
			definition = gets().chomp()
			geek[term] = definition
			print("#{term} has been redefined.\n")
		else
			print("Term not in dictionary\n")
		end
	# delete a term
	elsif choice == "4"
		print("Delete term: ")
		term = gets().chomp()
		if geek.include?(term)
			geek.delete(term)
			print("#{term} deleted from dictionary.\n")
		else
			print("Term not in dictionary.")
		end
	else
		print("Ivalid choice.")
	end

end


