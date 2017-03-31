from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Relation
from .models import Type
from .models import Pokemon
from .models import Profil

admin.site.register(Relation)
admin.site.register(Type)
admin.site.register(Pokemon)
admin.site.register(Profil)


# Register your models here.
