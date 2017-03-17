import json
import unicodedata

def foreign_key_type(nom_type):
	return{
		'Acier':     1,
		'Combat':    2,
	 	'Dragon':    3,
	 	'Eau':       4,
	 	'Electrik':  5,
	 	'Fée':       6,
	 	'Fee':       6,
	 	'Feu':       7,
	 	'Glace':     8,
	 	'Insecte':   9,
	 	'Normal':    10,
	 	'Plante':    11,
	 	'Poison':    12,
	 	'Psy':       13,
		'Roche':     14,
		'Sol':       15,
	 	'Spectre':   16,
	 	'Ténèbres':  17,
	 	'Tenebres':  17,
	 	'Vol':       18,
		'': 0
	}[nom_type]
	

def nom_image(num_poke):
	return (str(num_poke) + '.png')
	



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
			"type_pokemon": [foreign_key_type(value[3]), foreign_key_type(value[4])],
			"image_pokemon": nom_image(value[0]),
			"cout_pokemon": value[5]
		}
	})


json_string=json.dumps(new_data,ensure_ascii=False,
					   indent=4, separators=(',', ': '))	


print (json_string)
