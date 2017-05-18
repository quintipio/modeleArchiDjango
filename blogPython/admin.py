from django.contrib import admin
from .models import Categorie, Article, Message

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Message)