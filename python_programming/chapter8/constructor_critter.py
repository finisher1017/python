class Critter(object):

	def __init__(self):
		print("A new critter has been born!")

	def talk(self):
		print("\nHi, I'm an instance of class Critter.")

crit1 = Critter()
crit2 = Critter()

crit2.talk()
crit1.talk()