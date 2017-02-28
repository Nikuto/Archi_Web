from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sommaire/(\d+)$',views.sommaire_note,name='sommaire_note'),
    url(r'^sommaire/',views.sommaire,name='sommaire'),
    url(r'^date/$',views.date_actuelle,name='afficher_date'),
    url(r'^addition/(?P<nb1>\d+)/(?P<nb2>\d+)/$',views.addition,name='addition'),
    

]
