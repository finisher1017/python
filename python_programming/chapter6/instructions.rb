def instructions()
	"""Display game instructions."""
	print(
	"""

	Welcom to Tic-Tac-Toe.

	Make your move by entering a number 0 - 8.


			0 | 1 | 2
			---------
			3 | 4 | 5
			---------
			6 | 7 | 8

	"""
		)
end

# main
print("Here are the instructions to the Tic-Tac-Toe game: ")
instructions()
print("Here they are again:")
instructions()
print("You probably understand the game by now.")

print("\n\nPress the enter key to exit.")
gets().chomp()