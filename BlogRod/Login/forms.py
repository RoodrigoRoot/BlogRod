from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import logging

logging.basicConfig(
    level=logging.DEBUG
)

class LoginForm(forms.Form):

    username = forms.SlugField( help_text="Sin espacio, sin acentos ni caracteres especiales", required=True, label="Usuario",widget=forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(help_text="Introducir su contraseña",max_length=15, required=True, widget=forms.PasswordInput())

    def clean_username(self):
        username = str.lower(self.cleaned_data['username'])
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Este usuario no esta registrado")
        logging.debug("username"+username)
        return username
    
    def clean_password(self):
        
        username = str.lower(self.data['username'])
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        logging.debug("password"+username)
        if user and not user.check_password(password):
            raise ValidationError("Contaseña incorrecta")
        return password