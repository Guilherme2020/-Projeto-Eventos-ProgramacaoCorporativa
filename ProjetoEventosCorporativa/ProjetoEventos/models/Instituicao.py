
from django.db import models

class Instituicao(models.Model):
    cod_inst = models.IntegerField()
    nome_instituicao = models.CharField(max_length=45)
    local_instituicao = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)