<<<<<<< HEAD

from django.db import models

class Instituicao(models.Model):
    cod_inst = models.IntegerField()
    nome_instituicao = models.CharField(max_length=45)
=======
from django.db import models

class Instituicao(models.Model):
    nome = models.CharField(max_length=45)
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
    local_instituicao = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)