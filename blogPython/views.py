#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from blogPython.models import Article 
from blogPython.forms import ConnexionForm,ContactForm
from django.contrib.auth import logout,login, authenticate

def accueil(request):
    articles = Article.objects.all()
    return render(request,'blogPython/accueil.html',{'dernier_articles':articles})

def consulter_article(request,id_article,slug):
    article = get_object_or_404(Article,id=id_article,slug=slug)
    return render(request,'blogPython/consulter.html',{'article':article})

def editer_article(request,id_article,slug):
    return render(request,'blogPython/editerArticle.html')

def consulter_liste_article_date(request,mois,annee):
    return HttpResponse()

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid() : 
        sujet = form.cleaned_data['sujet']
        message=form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
            
    return render(request,'blogPython/contact.html',locals())

def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            
            if user:
                login(request,user)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request,'blogPython/connexion.html',locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))