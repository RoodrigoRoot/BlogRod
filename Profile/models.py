from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Profile(models.Model):

    LIKES = (("Programación"," Programación "),("Bases de Datos", "Bases de Datos"))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes_personals = models.CharField(("Gustos"), choices=LIKES, max_length=50)
    photo_profile = models.ImageField(("Imagen de Perfil"), upload_to="media/profile/photos/")
    slug = models.SlugField(("Slug"))
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.slug
    
def save_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.user.username)

pre_save.connect(save_slug, sender=Profile)
