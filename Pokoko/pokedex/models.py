from django.db import models

class Pokemon(models.Model):
	numeroPokemon = models.IntegerField
	nomPokemon = models.CharField(max_length=64)
	generationPokemon = models.IntegerField
	type1 = models.CharField(max_length=64)
	type2 = models.CharField(max_length=64)
	coutPokemon = models.IntegerField
