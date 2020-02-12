from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    slug = models.SlugField(("Slug"))
    photo_profile = models.ImageField(("Foto de perfil"), upload_to="media/profile/photos/")
    created_at = models.DateField(("Creacion"), auto_now=False, auto_now_add=True)
    modified_at = models.DateField(("Modificacion"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.slug
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

def create_slug_profile(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.user.username)

pre_save.connect(create_slug_profile, sender=Profile)      