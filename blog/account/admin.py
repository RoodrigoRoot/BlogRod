from django.contrib import admin
from .models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "premiun")
    search_fields = ("user__username",)
    
    def first_name(self, obj):
        return obj.user.first_name


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Premiun)