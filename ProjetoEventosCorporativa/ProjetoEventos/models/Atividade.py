
from django.db import models

from ProjetoEventos.models import Evento


class Atividade(models.Model):
    codigo_atividade = models.IntegerField()
    titulo = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    valor = models.FloatField()
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
