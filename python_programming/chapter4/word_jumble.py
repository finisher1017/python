import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINT = ("snake", "game name", "not difficult", "not easy", "AI", "never")

choice = random.randrange(len(WORDS))
word = WORDS[choice]
hint = HINT[choice]

correct = word

jumble = ""

while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

print("\nThe jumble is: ", jumble)
guess = input("\nYour guess: ")
while guess != correct and guess != " ":
	if guess == "hint":
		print(hint)
		guess = input("Your guess:")
	else:
		print("Sorry, that's incorrect.")
		guess = input("Your guess: ")



if guess == correct:
	print("Correct!\n")


input("\nPress enter to exit.")