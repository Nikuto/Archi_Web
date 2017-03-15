from django import template
from pokedex.forms import *

register = template.Library()

@register.assignment_tag
def recherche_form(format_string):
	return FiltreForm()
	
@register.assignment_tag
def recherche_pok(format_string):
	return PokemonForm()