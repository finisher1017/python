# positional parameters
def birthday1(name, age)
	print("Happy birthday #{name}! I hear you're #{age} today.\n")
end

# parameters with default values
def birthday2(name = "Jackson", age = 1)
	print("Happy birthday #{name}! I hear you're #{age} today.\n")
end


birthday1("Jackson", 1)
birthday1(1, "Jackson")
birthday1(name = "Jackson", age = 1)
birthday1(age = 1, name = "Jackson")

birthday2()
birthday2(name = "Katherine")
birthday2(age = 12)
birthday2(name = "Katherine", age = 12)
birthday2("Katherine", 12)

print("\n\nPress the enter key to exit.")
gets().chomp()