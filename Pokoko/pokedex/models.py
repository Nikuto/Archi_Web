from django.db import models

class Type(models.Model):
	nom_type = models.CharField(max_length=64)
	def __str__(self):
		return self.nom_type

class Pokemon(models.Model):
	numero_pokemon = models.IntegerField(default = 0)
	nom_pokemon = models.CharField(max_length=64)
	generation_pokemon = models.IntegerField(default = 0)
	type_pokemon = models.ManyToManyField(Type, blank=False)
	cout_pokemon = models.IntegerField(default = 0)
	def __str__(self):
		return self.nom_pokemon

class Relation(models.Model):
	type_offensif = models.ForeignKey(Type, related_name = 'type_offensif')
	type_defensif = models.ForeignKey(Type, related_name = 'type_defensif')
	relation = models.FloatField(default = 1)
	def __str__(self):
		return str(self.type_offensif) + ' / ' + str(self.type_defensif)