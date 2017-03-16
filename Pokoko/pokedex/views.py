from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from pokedex.forms import ConnexionForm
from .models import Pokemon
from .models import Type
from .models import Relation
from pokedex.forms import ConnexionForm,InscriptionForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.text import slugify

#Page d'accueil, a la racine du site
def index(request):
    
    return render(request,'pokedex/accueil.html')

#Page de sommaire, a /sommaire
def sommaire(request):
    return render(request,'test/sommaire.html')

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

def connexion(request):
    error = False
    if (request.method == "POST"):
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)#test de log
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return render(request, 'pokedex/accueil.html', locals())
            else: # sinon une erreur sera affichée
                error = True
        else:
            form = ConnexionForm()
    return render(request, 'pokedex/connexion.html', locals())

def deconnexion(request):

    logout(request)
    return redirect(reverse(connexion))

def inscription(request):
    error = False
    if (request.method == "POST"):
        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            mail = form.cleaned_data["mail"]
            User.objects.create_user(username,mail,password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
        else:
            form = InscriptionForm()
    return render(request,'pokedex/inscription.html',locals())

def filtre(request):
    error = False
    if(request.method == "POST"):
        form = FiltreSearch(request.POST)
        if form.if_valid():
            nom_pokemon = form.clean_data["nom"]
            pokemon = Pokemon.objects.get("nom_pokemon")
            return render(request, 'test/pokemon.html', {'pokemon' : pokemon})
        else:
            error = True
    else :
        form = FiltreSearch()
    return render(request,'pokedex/accueil.html',{"form":form})

def find(request):
    error = False
    if(request.method == "POST"):
        form = PokemonSearch(request.POST)
        if form.if_valid():
            nom_pokemon = form.clean_data["nom"]
            pokemon = Pokemon.objects.get(nom_pokemon__iexact = nom_pokemon)
            if(1):
                for type in pokemon.type_pokemon.all():
                    type_pokemon.append(type.nom_type)
                if len(type_pokemon) > 1:
                    type1 = type_pokemon[0]
                    type2 = type_pokemon[1]
                    return render(request, 'pokedex/pokemon.html', {'pokemon' : pokemon, 'type1': type1, 'type2': type2})
                else:
                    return render(request,'pokedex/accueil.html',{"form":form})
        else:
            error = True
    else :
        form = PokemonSearch()
    return render(request,'pokedex/accueil.html',{"form":form})


def type_to_key(nom_type):
    return{
        'Acier':     1,
        'Combat':    2,
        'Dragon':    3,
        'Eau':       4,
        'Electrik':  5,
        'Fée':       6,
        'Fee':       6,
        'Feu':       7,
        'Glace':     8,
        'Insecte':   9,
        'Normal':    10,
        'Plante':    11,
        'Poison':    12,
        'Psy':       13,
        'Roche':     14,
        'Sol':       15,
        'Spectre':   16,
        'Ténèbres':  17,
        'Tenebres':  17,
        'Vol':       18,
        '':           0,
        'NULL':       0,
    }[nom_type]


def pokemon_details_nom(request, nom_poke):
    pokemon = Pokemon.objects.get(nom_pokemon__iexact = nom_poke)
    print(pokemon)
    type_pokemon = []
    for type in pokemon.type_pokemon.all():
        type_pokemon.append(type.nom_type)
    if len(type_pokemon) > 1:
        type1 = type_pokemon[0]
        type2 = type_pokemon[1]
    type1_balance = Relation.objects.filter(type_defensif = type_to_key(type1))
    type2_balance = Relation.objects.filter(type_defensif = type_to_key(type2))
    balance = type1_balance
    if type2 != 'NULL':
        for type2, final in zip(type2_balance, balance):
            final.relation = final.relation * type2.relation
    return render(request, 'pokedex/pokemon.html', 
        {'pokemon' : pokemon, 'balance':balance})

def pokemon_details_numero(request, numero_poke):
    pokemon = Pokemon.objects.get(numero_pokemon = numero_poke)
    return render(request, 'pokedex/pokemon.html', 
        {'pokemon' : pokemon})

def pokedex(request):
    pokedex = Pokemon.objects.filter(numero_pokemon__lte = 50)
    return render(request, 'pokedex/pokemon_dex.html',
                    {'pokemon': pokedex})












