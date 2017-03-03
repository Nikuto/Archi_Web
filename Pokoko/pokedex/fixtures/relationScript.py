import json

tableType = [
	"Acier",
	"Combat",
	"Dragon",
	"Eau",
	"Electrik",
	"Fee",
	"Feu",
	"Glace",
	"Insecte",
	"Normal",
	"Plante",
	"Poison",
	"Psy",
	"Roche",
	"Sol",
	"Spectre",
	"Tenebres",
	"Vol"
]

relationTable = []

for attaque in tableType:
	for defense in tableType:
		relationTable.append({
			"model": "pokedex.relation",
			"fields": {
				"type_offensif": attaque,
				"type_defensif": defense,
				"relation": 1
			}
		})

json_string=json.dumps(relationTable,ensure_ascii=False,
					   indent=4, separators=(',', ': '))	

print (json_string)