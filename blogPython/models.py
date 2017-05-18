#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Utilisateur(models.Model):
    user = models.OneToOneField(User)
    inscrit_newsletter = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nom
    

class Article(models.Model):
    categories = models.ManyToManyField(Categorie, related_name="Categorie") 
    titre = models.CharField(max_length=150)
    auteur = models.ForeignKey("Utilisateur")
    datePublication = models.DateTimeField(auto_now=True, verbose_name="Date de parution")
    contenu = models.TextField(null=True)
    slug=models.SlugField(max_length=150)
    
    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    auteur = models.ForeignKey("Utilisateur")
    text = models.TextField(null=True)
    article = models.ForeignKey("Article")
    date = models.DateTimeField(auto_now=True, verbose_name="Date")
    
    def __str__(self):
        return self.text    
    

class Message(models.Model):
    origine = models.CharField(max_length=100)
    text = models.TextField(null=True)
    sujet = models.CharField(max_length=150)
    envoi = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    lu = models.BooleanField(default=False)

    def __str__(self):
        return self.sujet
    

class TraceAppli(models.Model):
    utilisateur = models.CharField(max_length=200)
    heure = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)
    
    def __str__(self):
        return "{} fait par {} à {}".format(self.action,self.utilisateur,self.heure)
