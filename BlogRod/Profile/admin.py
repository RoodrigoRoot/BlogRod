from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    
    fields = ("user", "photo_profile" )
    list_display = ("user", "slug", "created_at")


admin.site.register(Profile, ProfileAdmin)