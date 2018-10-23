puts "Enter starting point: "
start = gets().chomp()
puts "Enter ending point: "
finish = gets().chomp()
puts "Enter the count by: "
count = gets().chomp()
ran = (start..finish).step(count.to_i)
for i in ran
	puts i
end