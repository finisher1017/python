puts "Enter a word: "
word = gets().chomp()
new_word = []
word_length = word.length()

#while word_length > 0
#	new_word << word[word_length]
#	word_length -= 1
#end

while word_length != 0
	new_word << word[word_length - 1]
	word_length -= 1
end

p new_word.join()