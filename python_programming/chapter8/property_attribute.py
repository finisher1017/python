class Critter(object):

	def __init__(self, name):
		print("A new critter has been born!")
		self.__name = name

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		if new_name == "":
			print("Can't be empty.")
		else:
			self.__name = new_name
			print("Name change successful.")

	def talk(self):
		print("\nHi, I'm", self.name)


crit = Critter("Poochie")
crit.talk()

print("\ncritter's name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critter's name to Randolph...")
crit.name = "Randolph"

print("\ncritter's name is:", end=" ")
print(crit.name)

print("Attempting to change my critter's name to empty string...")
crit.name = ""

print("\ncritter's name is:", end=" ")
print(crit.name)
