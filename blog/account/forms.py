from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", help_text="Ingresa tu nombre de usuario", required=True)
    passwd = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        attrs={
            "placeholder":"Ingresa tu contraseña"
        }
    ))
    

    def clean_username(self):
        username = str.lower(self.cleaned_data["username"])
        if not User.objects.filter(username=username).exists():
            raise ValidationError("El usuario no existe")
        return username
    
    def clean_passwd(self):
        username = self.data["username"]
        password = self.cleaned_data["passwd"]
        user = User.objects.filter(username=username).first()
        if user and not user.check_password(password):
            raise Validation("Contraseña incorrecta")
        return password
        
    