
word = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
hint = ["snake", "game name", "not difficult", "not easy", "AI", "never"]

choice = rand(word.length())
word_choice = word[choice]
hint_choice = hint[choice]
word_count = word_choice.length()
jumble = ""
word_choice_arr = word_choice.split("")
jumbled_arr = []
while word_count != 0
	position = rand(word_count)
	jumbled_arr << word_choice_arr[position]
	word_choice_arr.delete_at(position)
	word_count -= 1
end
puts "The word is #{word_choice}"
puts "The jumbled word is #{jumbled_arr.join()}"

guess_count = 5
while guess_count != 0
	puts "Does the word contain the letter: "
	letter_guess = gets().chomp()
	if word_choice.include?(letter_guess)
		puts "Yes"
		guess_count -= 1
	else
		puts "No"
		guess_count -= 1
	end
end
puts "Guess the word: "
guess = gets().chomp()
while word_count == 0
	if guess == word_choice
		puts "Correct!"
		break
	else
		puts "Incorrect."
		puts "Guess the word: "
		guess = gets().chomp()
	end
end

