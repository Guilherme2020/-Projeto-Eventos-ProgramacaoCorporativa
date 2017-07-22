from django.db import models

from ProjetoEventos.models import Usuario


class Evento(models.Model):
    cod_evento = models.IntegerField()
    nome_evento = models.CharField(max_length=45)
    descricao  = models.CharField(max_length=45)
    data_inicio = models.CharField(max_length=45)
    data_fim = models.CharField(max_length=45)
    usuario_cod_user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
