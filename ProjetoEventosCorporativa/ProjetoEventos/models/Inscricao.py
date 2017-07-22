
from django.db import models

from ProjetoEventos.models import Evento, Usuario


class Inscricao(models.Model):
    cod_inscricao = models.IntegerField()
    data_inscricao = models.DateField()
    usuario_cod_user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    valor_total = models.FloatField()
