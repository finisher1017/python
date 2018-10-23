with open("test_write.txt", "w") as f:
	f.write("Hello World!")
with open("test_write.txt", "a") as f:
	f.write("\nWhat's the latest?")
with open("test_write.txt") as f:
	var = f.read()

print(var)