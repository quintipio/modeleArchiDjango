#-*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from blogPython import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accueil/$',views.accueil,name="accueil"),
    url(r'^accueil/(?P<page>\d+)$',views.accueil,name="accueil"),
    url(r'^articles/(?P<annee>\d{4})/(?P<mois>\d{2})$',views.consulter_liste_article_date,name="article_mois"),
    url(r'^article/(?P<id_article>\d+)-(?P<slug>.+)$',views.consulter_article,name="afficher_article"),
    url(r'^article_ajouter/$',views.ajouter_article,name="ajouter_article"),
    url(r'^article_modifier/(?P<id_article>\d+)-(?P<slug>.+)$',views.modifier_article,name="modifier_article"),
    url(r'^article_supprimer/(?P<id_article>\d+)-(?P<slug>.+)$',views.supprimer_article,name="supprimer_article"),
    url(r'^contact/$',views.contact, name='contact'),
    url(r'^connexion$',views.connexion,name="connexion"),
    url(r'^change_mdp$',auth_views.password_change),
    url(r'^change_mdp_done$',auth_views.password_change_done),
    url(r'^deconnexion$',views.deconnexion,name="deconnexion"),
]