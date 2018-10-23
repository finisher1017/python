inventory = ["sword", "armor", "shield", "potion"]

puts "Your inventory is: "
for i in inventory
	puts i
end

puts "\nYou have #{inventory.length()} items in your inventory"

if inventory.include?("potion")
	puts "You'll live."
end

puts "Enter index: "
ind = gets().chomp().to_i
puts "At index #{ind} is #{inventory[ind]}"

puts "Enter start: "
start = gets().chomp().to_i
puts "Enter end: "
finish = gets().chomp().to_i
puts inventory[start..finish]

chest = ["gold", "gems"]
puts "You find a chest that contains: "
puts chest
puts "\nYou add the contents of the chest to your inventory."
inventory << chest
puts "Your inventory is now: "
puts inventory

puts "\nYou trade your sword for a crossbow."
inventory[0] = "crossbow"
puts "Your inventory is now:"
puts inventory

puts "\nYou use your gold and gems to buy an orb."
inventory[4..6] = ["orb"]
puts "Your inventory is now: "
puts inventory

puts "\nYour lose your shield in battle."
inventory.delete("shield")
puts "Your inventory is now: "
puts inventory

puts "\nYour crossbow and armor are stolen by thieves."
inventory.delete("crossbow")
inventory.delete("armor")
puts "Your inventory is now: "
puts inventory