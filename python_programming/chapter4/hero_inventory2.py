inventory = ("sword", "armor", "shield", "potion")

print("Your items:")
for i in inventory:
	print(i)

print("You have", len(inventory), "items in your possession.")

if "potion" in inventory:
	print("\n You'll live to fight another day.")


index = int(input("\nEnter the index number: "))
print("At index", index, "is", inventory[index])

start = int(input("\nEnter beginning index: "))
finish = int(input("\nEnter ending index: "))
print("inventory[", start, ":", finish, "] is", end=" ")
print(inventory[start:finish])

chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print(inventory)

input("\nPress enter to continue.")