from django.db import models


# Create your models here.
class Campanha(models.Model):
    objects = None
    titulo_campanha = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='campanhas/imagens/')
    #pub_date = models.DateField('date published', default="2020-01-01")
