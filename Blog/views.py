from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from Article.models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
class IndexView(View):

    def get(self, request, *args, **kwargs):
        article = Article.objects.last()      
        
        return render(request, "index.html", locals())




def logout_view(request):
    logout(request)
    return redirect(reverse("home"))

class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', locals())

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=user, password=password)
            
            if user is not None:
               login(request, user)
               return redirect(reverse("home"))
            else:
                messages.error(request,'Usuario o Contraseña incorrecta')
                return redirect('login')

        else:
            form = LoginForm()
        return render(request, 'login.html', locals())
