

from django.db import models

from ProjetoEventos.models import Instituicao, Evento


class Apoio(models.Model):
    instituicao_cod_inst = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
    eventos_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    cod_apoio = models.DecimalField()
