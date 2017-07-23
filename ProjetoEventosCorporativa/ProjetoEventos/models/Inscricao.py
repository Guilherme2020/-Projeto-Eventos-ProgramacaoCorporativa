from django.db import models

import Evento, Usuario, Estado_Inscricao

class Inscricao(models.Model):
    usuario_cod = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_inscricao = models.DateField()
    valor_total = models.FloatField()
    evento_cod = models.ForeignKey(Evento, on_delete=models.CASCADE)
    pagamento = models.DateField()
    estado = models.ForeignKey(Estado_Inscricao, on_delete=models.CASCADE)
