word = input("Enter a word: ")

new_word = ""

count = len(word)

while count > 0:
	new_word += word[count - 1]
	count -= 1

print(new_word)