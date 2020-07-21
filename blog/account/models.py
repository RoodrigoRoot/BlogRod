from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Premiun(models.Model):
    name = models.CharField(verbose_name=("Premiun"), max_length=50)
    status = models.BooleanField(verbose_name=(""), default=False)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Premiun"
        verbose_name_plural = "Premiun"



class Profile(models.Model):
    
    user = models.OneToOneField(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name=("Foto de Perfil"), upload_to="profile")
    premiun = models.ForeignKey(Premiun, verbose_name=("Premiun"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        
        
