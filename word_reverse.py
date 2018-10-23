phrase = "Hello World"
first_word = []
second_word = []

for i in phrase:
	first_word.append(i)
	if i == " ":
		first_word.insert(0,i)
		sw = second_word.append(i).join(second_word)
		first_word.insert(0, sw)

print(first_word)

