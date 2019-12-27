from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginFasdorm(forms.Form):
    username = forms.SlugField(label='Username', help_text='Sin espacios, sin acentos, sin ñ / puedes usar - y _', 
        required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')

    def clean_username(self):
        username = str.lower(self.cleaned_data['username'])
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Este usuario no esta registrado")
        return username

    def clean_password(self):
        username = self.data['username']
        password = self.cleaned_data['password']
        user = User.objects.filter(username=username).first()
        if user and not user.check_password(password):
            raise ValidationError("Contraseña incorrecta")
        return password

class LoginForm(forms.Form):
    username = forms.SlugField(label="Usuario", allow_unicode=False, required=True, help_text="Por favor ingresar tu nombre de usuario.")
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')