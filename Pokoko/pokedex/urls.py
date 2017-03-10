from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sommaire/(\d+)$',views.sommaire_note,name='sommaire_note'),
    url(r'^sommaire/',views.sommaire,name='sommaire'),
    url(r'^date/$',views.date_actuelle,name='afficher_date'),

    url(r'^connexion/',views.connexion,name='connexion'),
    url(r'^deconnexion/', views.deconnexion, name='deconnexion'),
    url(r'^inscription/',views.inscription,name='inscription'),
   

    url(r'^addition/(?P<nb1>\d+)/(?P<nb2>\d+)/$',views.addition,name='addition'),

    
    url(r'^pokemon/',views.pokemon,name='pokemon'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
