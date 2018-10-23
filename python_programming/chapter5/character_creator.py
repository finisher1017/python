character = input("Enter character name: ")
pool = 30
attributes = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0}
choose_attr = input("Choose attribute: ")
points_add = int(input("Add points: "))
attributes[choose_attr] = points_add
pool -= points_add
print(attributes)
print(pool)