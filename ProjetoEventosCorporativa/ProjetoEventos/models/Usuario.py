

from django.db import models


class Usuario(models.Model):
    cod_user = models.IntegerField()
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)



