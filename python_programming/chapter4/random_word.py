import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = random.choice(WORDS)
print("\nThere are", len(word), "letters in the word.")
guess_count = 5

while guess_count != 0:
	guess_letter = input("Does the word contain: ")
	if guess_letter in word:
		print("Yes")
		guess_count -= 1
	else:
		print("No")
		guess_count -= 1


guess = input("Guess the word: ")
if guess == word:
	print("Correct!")
else:
	print("Sorry, that's incorrect.")