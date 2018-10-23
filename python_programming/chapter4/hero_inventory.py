inventory = ()

if not inventory:
	print("You are empty-handed.")


input("\nPress the enter key to continue.")

inventory = ("sword", "armor", "shield", "potion")

print("\nThe tuple inventory is:")
print(inventory)
print("\nYour items:")
for i in inventory:
	print(i)