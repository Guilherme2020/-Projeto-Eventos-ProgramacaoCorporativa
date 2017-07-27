from django.db import models

<<<<<<< HEAD
from ProjetoEventos.models import Usuario


class Evento(models.Model):
    cod_evento = models.IntegerField()
    nome_evento = models.CharField(max_length=45)
    descricao  = models.CharField(max_length=45)
    data_inicio = models.CharField(max_length=45)
    data_fim = models.CharField(max_length=45)
    usuario_cod_user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
=======
import Usuario, Tipo_Evento, Estado_Evento, Cupom

class Evento(models.Model):
    nome = models.CharField(max_length=45)
    tipo_evento = models.ForeignKey(Tipo_Evento, on_delete = models.CASCADE)
    estado_evento = models.ForeignKey(Estado_Evento, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    cupom = models.ForeignKey(Cupom, on on_delete=CASCADE)
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
