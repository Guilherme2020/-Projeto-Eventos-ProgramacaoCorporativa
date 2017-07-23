from django.db import models

import Evento, TipoAtividade

class Atividade(models.Model):
    nome = models.CharField(max_length=45)
    tipoAtividade = models.ForeignKey(TipoAtividade, on_delete = models.CASCADE)
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    valor = models.FloatField()
