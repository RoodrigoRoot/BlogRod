from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.
import logging

logging.basicConfig(
    level=logging.DEBUG
)

class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")
        forms = LoginForm()
        return render(request, "login/login.html", locals())
    
    def post(self, request, *args, **kwargs):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                return redirect("login")   
        else:
            
            error = "Credenciales incorrectas"
            forms = LoginForm()
        return render(request, 'login/login.html', locals())

                