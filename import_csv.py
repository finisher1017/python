import csv

with open("coding_projects.csv") as c:
	contents = csv.reader(c)
	lc = []
	for i in contents:
		lc += i

print(lc)