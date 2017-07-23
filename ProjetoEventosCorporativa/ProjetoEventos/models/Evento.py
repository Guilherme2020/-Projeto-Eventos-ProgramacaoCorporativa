from django.db import models

import Usuario, Tipo_Evento, Estado_Evento, Cupom

class Evento(models.Model):
    nome = models.CharField(max_length=45)
    tipo_evento = models.ForeignKey(Tipo_Evento, on_delete = models.CASCADE)
    estado_evento = models.ForeignKey(Estado_Evento, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    cupom = models.ForeignKey(Cupom, on on_delete=CASCADE)
