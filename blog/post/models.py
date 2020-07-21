from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name=("Titulo"), max_length=50)
    content = models.TextField(verbose_name=("Contenido"))
    author = models.ForeignKey("account.Profile", verbose_name=("Perfil"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        
    