import json
import unicodedata


pokedex_data=json.load(open("./oldPokemon.json"))


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
			"type_pokemon": [value[3], value[4]],
			"cout_pokemon": value[5]
		}
	})


json_string=json.dumps(new_data,ensure_ascii=False,
					   indent=4, separators=(',', ': '))	

json_string = unicodedata.normalize('NFKD', json_string).encode('ASCII', 'ignore')

print json_string
