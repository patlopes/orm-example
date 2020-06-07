from django.db import models

# Create your models here.
class UsuarioModel(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()