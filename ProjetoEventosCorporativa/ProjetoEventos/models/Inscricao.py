<<<<<<< HEAD

from django.db import models

from ProjetoEventos.models import Evento, Usuario


class Inscricao(models.Model):
    cod_inscricao = models.IntegerField()
    data_inscricao = models.DateField()
    usuario_cod_user = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    valor_total = models.FloatField()
=======
from django.db import models

import Evento, Usuario, Estado_Inscricao

class Inscricao(models.Model):
    usuario_cod = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_inscricao = models.DateField()
    valor_total = models.FloatField()
    evento_cod = models.ForeignKey(Evento, on_delete=models.CASCADE)
    pagamento = models.DateField()
    estado = models.ForeignKey(Estado_Inscricao, on_delete=models.CASCADE)
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
