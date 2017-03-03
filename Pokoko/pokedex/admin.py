from django.contrib import admin

from .models import Relation
from .models import Type
from .models import Pokemon

admin.site.register(Relation)
admin.site.register(Type)
admin.site.register(Pokemon)
# Register your models here.
