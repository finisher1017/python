import json

my_info = {
	"first_name": "Jonathan",
	"last_name": "Seubert",
	"age": 37,
}
with open("info_dic.json", "w") as f:
	json.dump(my_info, f)