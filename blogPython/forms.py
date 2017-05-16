#-*- coding: utf-8 -*-
from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre email")
    renvoi = forms.BooleanField(label="Obtenir une copie",required=False)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if 'pizza' in message:
            raise forms.ValidationError("Pas de pizza ici !")
        
        return message
    
    def clean(self):
        cleaned_data = super(ContactForm,self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')
        
        if sujet and message:
            if'pizza' in sujet and 'pizza' in message:
                msg = "Vous parlez de pizza dans le sujet le message"
                self.add_error("message",msg)
            
        return cleaned_data