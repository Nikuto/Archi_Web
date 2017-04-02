from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .models import Pokemon
from .models import Type
from .models import Relation
from pokedex.forms import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
 

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
                return redirect('index')
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
            passwordve = form.cleaned_data["passwordverif"]
            mail = form.cleaned_data["mail"]
            if(password != passwordve):
                return redirect('index')
            User.objects.create_user(username,mail,password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                error = True
        else:
            form = InscriptionForm()
    return render(request,'pokedex/inscription.html',locals())

def filtre(request):
    error = False
    nb=False
    if(request.method == "POST"):

        form = FiltreForm(request.POST)
        if form.is_valid():

            type1 = form.cleaned_data["typeun"]
            type2 = form.cleaned_data["typedeux"]
            gen = form.cleaned_data["gen"]

            pokedex = Pokemon.objects.all()

            if (type1 != "-1"):
                pokedex = pokedex.filter(type_pokemon = type1)
                print(type1)
                nb = True
            if (type2 != "-1"):
                pokedex = pokedex.filter(type_pokemon = type2)
                print(type1)
                nb = True
            if(gen != "-1"):
                print(gen)
                pokedex = pokedex.filter(generation_pokemon = gen)
                nb = True
            if(nb):
                return render(request, 'pokedex/pokemon_dex.html', {'pokemon': pokedex})
        else:
            error = True
    
    else :
        form = FiltreForm()
    
    return redirect('index')

def find(request):
    error = False
    if(request.method == "POST"):
        form = PokemonForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            try:
                pokemon = Pokemon.objects.get(nom_pokemon__iexact = nom)
                return redirect('pokemon_details_nom',nom_poke=nom)
            except ObjectDoesNotExist as e:
                return redirect('index')
        else:
            form = PokemonForm()
    return redirect('index')


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

def balance_pokemon(pokemon):
    type_pokemon = []
    for type in pokemon.type_pokemon.all():
        type_pokemon.append(type.nom_type)
    type1_balance = Relation.objects.filter(type_defensif = type_to_key(type_pokemon[0]))
    type2_balance = Relation.objects.filter(type_defensif = type_to_key(type_pokemon[1]))
    balance = type2_balance
    if type_pokemon[0] != 'NULL':
        for type1, final in zip(type1_balance, balance):
            final.relation = final.relation * type1.relation
    return balance


def pokemon_details_nom(request, nom_poke):
    pokemon = Pokemon.objects.get(nom_pokemon__iexact = nom_poke)
    print(pokemon)
    type_pokemon = []
    balance = balance_pokemon(pokemon)
    return render(request, 'pokedex/pokemon.html', 
        {'pokemon' : pokemon, 'balance':balance})

def pokemon_details_numero(request, numero_poke):
    pokemon = Pokemon.objects.get(numero_pokemon = numero_poke)
    return render(request, 'pokedex/pokemon.html', 
        {'pokemon' : pokemon})

def pokedex(request):
    pokedex = Pokemon.objects.filter(generation_pokemon = 1)
    return render(request, 'pokedex/pokemon_dex.html',
                    {'pokemon': pokedex})


def ajout(request,nom_poke):
    user = User.objects.get(username=request.user.username)
    if(user.profil.pokemon_equipe.count() < 6):
        user.profil.pokemon_equipe.add(Pokemon.objects.get(nom_pokemon__iexact = nom_poke))
        user.save()
    return redirect('pokemon_details_nom',nom_poke=nom_poke);
    # if(User.is_authenticated):
    #     return HttpResponse("C {0}".format(Pokemon.objects.get(nom_pokemon__iexact = nom_poke)))
    # return HttpResponse("Salut, anonyme.")

def equipe(request):
    if(User.is_authenticated):
        user = User.objects.get(username=request.user.username)
        equipe = user.profil.pokemon_equipe.all()
        return render(request, 'pokedex/equipe.html',{'pokemon': equipe})
    return redirect('index')

def profil(request):

    if(User.is_authenticated):
        return render(request,'pokedex/profil.html')
    else:
        return redirect('inscription')

    return redirect('index')







