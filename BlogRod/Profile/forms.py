from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileRegisterForm(forms.ModelForm):

    model = Profile
    fields = ("photo_profile", "")