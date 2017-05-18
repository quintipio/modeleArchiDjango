#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views.decorators.cache import cache_page
from blogPython.models import Article,Message
from blogPython.forms import ConnexionForm, ContactForm, ArticleForm


def accueil(request,page=1):
    #articles = Article.objects.all().order_by('-id')[:5] récupère les 5 derniers
    articles = Article.objects.all().order_by('-id')
    paginator = Paginator(articles,3)
    try:
        articles_page = paginator.page(page)
    except EmptyPage:
        articles_page = paginator.page(paginator.num_pages)
    return render(request,'blogPython/accueil.html',locals())


@cache_page(300) #5 fois 60secondes
def consulter_article(request, id_article, slug):
    article = get_object_or_404(Article, id=id_article, slug=slug)
    return render(request,'blogPython/consulter.html', {'article': article})

@login_required 
def modifier_article(request, id_article, slug):
    article = get_object_or_404(Article, id=id_article, slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        article.auteur = request.user.utilisateur
        article.slug = slugify(article.titre)
        article.categories = form.cleaned_data['categories']
        article.save()   
        messages.success(request,"Votre article a bien été mis à jour")
        return redirect(reverse(accueil))
    return render(request,'blogPython/editerArticle.html',locals())

@login_required
def supprimer_article(request, id_article, slug):
    article = get_object_or_404(Article, id=id_article, slug=slug)
    article.delete()      
    messages.success(request,"Votre article a bien été supprimé")
    return redirect(reverse(accueil))


@login_required
def ajouter_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.auteur = request.user.utilisateur
        article.slug = slugify(article.titre)
        article.save()
        form.save_m2m()
        messages.success(request,"Votre article a bien été ajouté")
        return redirect(reverse(accueil))
    return render(request, 'blogPython/ajouterArticle.html', locals())


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
        messages.infos(request,"Votre message a été envoyé")

        if renvoi:
            try :
                send_mail(sujet, message, "donotreply@noreply.fr", [envoyeur])
            except :
                form.add_error("message","Erreur lors de l'envoi du mail")
                messages.error(request,"Erreur lors de l'envoi du mail")
            
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