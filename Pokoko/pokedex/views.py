from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#Page d'acceuil, a la racine du site
def index(request):
	
    return render(request,'pokedex/acceuil.html')

#Page de sommaire, a /sommaire
def sommaire(request):
	return HttpResponse("Oep,le sommaire")

#page d'un sommaire precis, a /sommaire/X
def sommaire_note(request,id_sommaire):
	if int(id_sommaire) > 100:
		raise Http404

	return HttpResponse("Tu demandes le sommaire {0} ? J'ai rien fait dmg.".format(id_sommaire))

#Test pour afficher la date
def date_actuelle(request):
	return render(request, 'test/date.html',{'date':datetime.now()})

#Test pour additionner
def addition(request,nb1,nb2):
	total = int(nb1) + int(nb2)

	return render(request,'test/addition.html',locals())
