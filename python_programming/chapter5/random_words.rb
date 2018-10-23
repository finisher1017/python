words = ["OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON"]
new_words = []

while words.length() > 0
	choice = rand(words.length())
	word_choice = words[choice]
	print(word_choice + "\n")
	if new_words.include?(word_choice)
		next
	else
		new_words << word_choice
		words.delete(word_choice)
	end
end
