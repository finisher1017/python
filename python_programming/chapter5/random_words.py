import random

words = ["OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON"]
new_words = []

while len(words) > 0:
	choice = random.randrange(len(words))
	word_choice = words[choice]
	print(word_choice)
	if word_choice in new_words:
		next
	else:
		new_words.append(word_choice)
		del words[choice]

print(new_words)
