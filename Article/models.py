from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(("Nombre del Articulo"), max_length=50, null=False, blank=False)
    image = models.ImageField(("Imagen para el articulo"), upload_to="media/article/photos/")
    subtitle = models.CharField(("Subtitulo"), null=True, blank=True, max_length=16)
    content = models.TextField(("Informacion"))

    def __str__(self):
        return self.name