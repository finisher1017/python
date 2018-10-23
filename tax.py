import json

stubs_count = 23
total = 0
pay_stubs = []

while stubs_count > 0:
	stub_amount = input("Enter amount: ")
	pay_stubs.append(int(stub_amount))
	stubs_count -= 1

with open("tax_totals.json", "w") as f:
	json.dump(pay_stubs, f)

with open("tax_totals.json") as f:
	totals = json.load(f)

for i in totals:
	total += i

print(total)