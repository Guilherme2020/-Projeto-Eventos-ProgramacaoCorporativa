



from django.db import models
from ProjetoEventos.models import Evento



class Cupom(models.Model):

    cod_cupom = models.DecimalField(primary_key=True)
    data_validade = models.DateField()
    eventos_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
