from django import forms
from pokedex.choices import *


class ConnexionForm(forms.Form):
  username = forms.CharField(label="Nom d'utilisateur", max_length=30)
  password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class InscriptionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	passwordverif = forms.CharField(label="Retapez votre mot de passe", widget=forms.PasswordInput)
	mail = forms.EmailField(label="eMail")

class PokemonForm(forms.Form):
	nom = forms.CharField(label="Nom du pokemon", max_length=30,required=False)
	
class FiltreForm(forms.Form):
	typeun = forms.ChoiceField(choices=TYPE_CHOICES,label="Type",initial='',widget=forms.Select(),required=False);
	typedeux = forms.ChoiceField(choices=TYPE_CHOICES,label="Second type",initial='',widget=forms.Select(),required=False);
	gen = forms.ChoiceField(choices=GEN_CHOICES,label="Génération",initial='',widget=forms.Select(),required=False);
	