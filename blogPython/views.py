#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from blogPython.models import Article,Message
from blogPython.forms import ConnexionForm, ContactForm, ArticleForm
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.defaultfilters import slugify


def accueil(request):
    articles = Article.objects.all().order_by('-id')[:5]
    return render(request,'blogPython/accueil.html',{'dernier_articles':articles})


def consulter_article(request, id_article, slug):
    article = get_object_or_404(Article, id=id_article, slug=slug)
    return render(request,'blogPython/consulter.html', {'article': article})


@login_required
def editer_article(request, id_article, slug):
    article = get_object_or_404(Article, id=id_article, slug=slug)

    return render(request,'blogPython/editerArticle.html')


@login_required
def ajouter_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        form.auteur = request.user.utilisateur
        form.slug = slugify(form.titre)
        form.save()
    return render(request, 'blogPython/editerArticle.html', locals())


def consulter_liste_article_date(request, mois, annee):
    return HttpResponse()


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        message_sauvegarder = Message()
        message_sauvegarder.sujet = sujet
        message_sauvegarder.origine = envoyeur
        message_sauvegarder.text = message
        message_sauvegarder.save()

        if renvoi:
            try :
                send_mail(sujet, message, "donotreply@noreply.fr", [envoyeur])
            except :
                form.add_error("message","Erreur lors de l'envoi du mail")
            
    return render(request, 'blogPython/contact.html', locals())


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            
            if user:
                login(request,user)
                return redirect(reverse(accueil))
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'blogPython/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))