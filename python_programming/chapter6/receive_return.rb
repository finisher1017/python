def display(message)
	print(message)
end

def give_me_five()
	five = 5
	return five
end

def ask_yes_no(question)
	"""Ask a yes or no question"""
	response = ""
	until response == "y" or response == "n"
		print(question) 
		response = gets().chomp()
	end
	return response
end


# main
display("Here's a messge for you.\n")

number = give_me_five()
print("Here's what I got from give_me_five(): #{number}")

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering: #{answer}")

print("\n\nPress the enter key to exit.")
gets().chomp()