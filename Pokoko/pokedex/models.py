from django.db import models
from django.contrib.auth.models import User

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
<<<<<<< HEAD
		return self.type_offensif + "/" + self.type_defensif

class Profil(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(blank=True,upload_to="avatars/")

	def __str__(self):
		return "Profil de {0}".format(self.user.username)
=======
		return str(self.type_offensif) + ' / ' + str(self.type_defensif)
>>>>>>> 51d7681f689fde5a7d337066ea97a6003b0db6cd
