#-*- coding: utf-8 -*-
from django import forms
from blogPython.models import Article

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre email",max_length=150)
    renvoi = forms.BooleanField(label="Obtenir une copie",required=False)

    def clean(self):
        cleaned_data = super(ContactForm,self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')
        if sujet and message:
            if'spam' in sujet and 'spam' in message:
                msg = "Vous parlez de spam dans le sujet et le message"
                self.add_error("message",msg)
            
        return cleaned_data