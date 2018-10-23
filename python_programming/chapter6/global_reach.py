def read_global():
	print("From inside the local scope of read_global(), value is:", value)

def shadow_global():
	value = -10
	print("From inside the local scope shadow_global, value is", value)

def change_global():
	global value
	value = -10
	print("From inside the local scope of change_global(), value is:", value)

#main - global scope

value = 10
print("In the global scope, value has been set to:", value, "\n")

read_global()
print("Back in the global, value has now changed to:", value, "\n")

shadow_global()
print("Back in the global scope, value is still", value, "\n")

change_global()
print("Back in the global scope, value has now changed to:", value, "\n")

input("Exit")