import json

data = []
pokedex_data=json.load(open("./pokemon.json"))


new_data = []
#print (pokedex_data)
#print (pokedex_data["values"])

for value in pokedex_data["values"]:
	new_data.append({"model": "myapp.person"})

json_string=json.dumps(new_data,ensure_ascii=False, sort_keys=True,
					   indent=4, separators=(',', ': '))	

print (json_string)
