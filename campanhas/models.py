from django.db import models


# Create your models here.
class Campanha(models.Model):
    titulo_campanha = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='imagens/')
