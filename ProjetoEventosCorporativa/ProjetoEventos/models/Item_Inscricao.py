

from django.db import models

from ProjetoEventos.models import Atividade, Evento, Inscricao,Cupom


class Item_Inscricao(models.Model):
    atividade_cod_atividade = models.ForeignKey(Atividade,on_delete=models.CASCADE)
    inscricao_cod_inscricao = models.ForeignKey(Inscricao,on_delete = models.CASCADE)
    cod_item  = models.IntegerField()
    cupom_cod_cupom = models.ForeignKey(Cupom,on_delete = models.CASCADE)
    cupom_evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
