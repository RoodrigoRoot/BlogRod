from django.shortcuts import render
from django.views import View
from .forms import *

# Create your views here.

class ProfileView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "profile.html", locals())
