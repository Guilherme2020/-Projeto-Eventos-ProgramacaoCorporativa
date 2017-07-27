<<<<<<< HEAD




from django.db import models
from ProjetoEventos.models import Evento



class Cupom(models.Model):

    cod_cupom = models.IntegerField()
    data_validade = models.DateField()
    eventos_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
=======
from django.db import models

import Evento

class Cupom(models.Model):
    cod_cupom = models.CharField(max_length=45)
    desconto = models.IntegerField()
    data_validade = models.DateField()
    eventos_cod = models.ForeignKey(Evento,on_delete=models.CASCADE)
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
