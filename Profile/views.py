from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
# Create your views here.

class ProfileUserView(LoginRequiredMixin,  DetailView):
    model = Profile
    login_url = '/login/'
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
