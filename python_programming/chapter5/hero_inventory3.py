inventory = ["sword", "armor", "shield", "potion"]

print("Your items: ")
for i in inventory:
	print(i)

print("\nYou have", len(inventory), "items in your inventory.")

if "potion" in inventory:
	print("You'll live.")

index = int(input("Enter the index: "))
print("At index", index, "is", inventory[index])

start = int(input("Enter start: "))
finish = int(input("Enter end: "))
print(inventory[start:finish])

chest = ["gold", "gems"]
print("You find a chest which contains:")
for i in chest:
	print(i)

print("\nYou add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now: ")
for i in inventory:
	print(i)

print("\nYou trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now:\n")
print(inventory)

print("\nYou use your gold and gems to buy an orb.")
inventory[4:6] = ["orb"]
print("\nYour inventory in now:\n")
for i in inventory:
	print(i)

print("You lose your shield in battle.")
del inventory[2]
print("Your inventory is now:\n")
for i in inventory:
	print(i)

print("\nYour crossbow and armor are stolen by thieves.")
del inventory[:2]
print("Your inventory is now: ")
print(inventory)