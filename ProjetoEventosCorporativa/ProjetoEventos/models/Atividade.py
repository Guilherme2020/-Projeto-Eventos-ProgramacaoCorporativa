<<<<<<< HEAD

from django.db import models

from ProjetoEventos.models import Evento


class Atividade(models.Model):
    codigo_atividade = models.IntegerField()
    titulo = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    valor = models.FloatField()
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
=======
from django.db import models

import Evento, TipoAtividade

class Atividade(models.Model):
    nome = models.CharField(max_length=45)
    tipoAtividade = models.ForeignKey(TipoAtividade, on_delete = models.CASCADE)
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    valor = models.FloatField()
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
