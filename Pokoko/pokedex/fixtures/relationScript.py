import json
import unicodedata

def foreign_key_type(nom_type):
	return{
		'Acier':     "type : 1",
		'Combat':    "type : 2",
	 	'Dragon':    "type : 3",
	 	'Eau':       "type : 4",
	 	'Electrik':  "type : 5",
	 	'Fée':       "type : 6",
	 	'Fee':       "type : 6",
	 	'Feu':       "type : 7",
	 	'Glace':     "type : 8",
	 	'Insecte':   "type : 9",
	 	'Normal':    "type : 10",
	 	'Plante':    "type : 11",
	 	'Poison':    "type : 12",
	 	'Psy':       "type : 13",
		'Roche':     "type : 14",
		'Sol':       "type : 15",
	 	'Spectre':   "type : 16",
	 	'Ténèbres':  "type : 17",
	 	'Tenebres':  "type : 17",
	 	'Vol':       "type : 18",
		'': ""
	}[nom_type]
	 

relation_data[]=json.load(open("relation.json"))

json_string=json.dumps(relation_data,ensure_ascii=False,
					   indent=4, separators=(',', ': '))	

print (json_string)












