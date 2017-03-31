from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.fields.related import OneToOneField


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
	image_pokemon = models.FileField(upload_to='pokemon', default='0.png')
	def __str__(self):
		return self.nom_pokemon

class Relation(models.Model):
	type_offensif = models.ForeignKey(Type, related_name = 'type_offensif')
	type_defensif = models.ForeignKey(Type, related_name = 'type_defensif')
	relation = models.FloatField(default = 1)
	def __str__(self):
		return str(self.type_offensif) + " / " + str(self.type_defensif)

class Profil(models.Model):

	user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE,related_name='profil')
	avatar = models.ImageField(blank=True,upload_to="avatars/")
	pokemon_equipe = models.ManyToManyField(Pokemon, blank = True)
	def __str__(self):
		return "Profil de {0}".format(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profil.save()  