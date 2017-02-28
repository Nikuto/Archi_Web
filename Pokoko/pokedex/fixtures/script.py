import json

pokedex_data=json.load(open("./pokemon.json"))


new_data = []
#print (pokedex_data)
#print (pokedex_data["values"])

for value in pokedex_data["values"]:
	new_data.append({
		"model": "pokedex.pokemon",
		"fields": {
			"numero_pokemon": value[0],
			"nom_pokemon": value[1],
			"generation_pokemon": value[2],
			"type_pokemon_1": value[3],
			"type_pokemon_2": value[4],
			"cout_pokemon": value[5]
		}
	})

json_string=json.dumps(new_data,ensure_ascii=False,
					   indent=4, separators=(',', ': '))	

print (json_string)
