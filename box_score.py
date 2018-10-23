fight = {
	"fighter1": {
		"round1": 0,
		"round2": 0
	},

	"fighter2": {
		"round1": 0,
		"round2": 0
	}
}

fight["fighter1"]["round1"] = 10
fight["fighter2"]["round1"] = 9
fight["fighter1"]["round2"] = 10
fight["fighter2"]["round2"] = 9
print(fight)