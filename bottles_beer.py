def bottles_of_beer(bob):
	if bob < 1:
		print("No more bottles")
		return

	tmp = bob
	bob -= 1

	print("{}, {}, {}".format(tmp,tmp,bob))
	bottles_of_beer(bob)

bottles_of_beer(99)