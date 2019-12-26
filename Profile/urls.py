from django.urls import path
from .views import *

urlpatterns = [
    path("profile/<slug:slug>/", ProfileUserView.as_view(), name="profile")
]
