



from django.db import models
from ProjetoEventos.models import Evento



class Cupom(models.Model):

    cod_cupom = models.IntegerField()
    data_validade = models.DateField()
    eventos_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
