from django.db import models

import Evento

class Cupom(models.Model):
    cod_cupom = models.CharField(max_length=45)
    desconto = models.IntegerField()
    data_validade = models.DateField()
    eventos_cod = models.ForeignKey(Evento,on_delete=models.CASCADE)
