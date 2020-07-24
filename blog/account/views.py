from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm
from django.contrib.auth import logout, authenticate, login

# Create your views here.

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "account/login.html", locals())
    
    
    def post(self, request, *args, **kwargs):
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['passwd']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
        else:
            form = LoginForm()
        return render(request, 'account/login.html', locals())
    
def logout_view(request):
    logout(request)
    return redirect(reverse("home"))