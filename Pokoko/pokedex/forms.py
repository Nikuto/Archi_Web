from django import forms

class ConnexionForm(forms.Form):
  username = forms.CharField(label="Nom d'utilisateur", max_length=30)
  password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class InscriptionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	passwordverif = forms.CharField(label="Retapez votre mot de passe", widget=forms.PasswordInput)
	mail = forms.EmailField(label="eMail")

