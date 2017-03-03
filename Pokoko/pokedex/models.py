from django.db import models

class Type(models.Model):
	nom_type = models.CharField(max_length=64)

class Pokemon(models.Model):
	numero_pokemon = models.IntegerField(default = 0)
	nom_pokemon = models.CharField(max_length=64)
	generation_pokemon = models.IntegerField(default = 0)
	type_pokemon = models.ManyToManyField(Type)
	cout_pokemon = models.IntegerField(default = 0)

class Relation(models.Model):
	type_offensif = models.ForeignKey(Type, related_name = 'type1')
	type_defensif = models.ForeignKey(Type, related_name = 'type2')
	relation = models.IntegerField(default = 1)