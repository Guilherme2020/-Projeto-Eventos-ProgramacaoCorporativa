from django.db import models

import Instituicao, Evento, Tipo_ApoioRealizacao

class Apoio_Realizacao(models.Model):
    instituicao_cod = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
    eventos_cod = models.ForeignKey(Evento,on_delete=models.CASCADE)
    tipo_ApoioRealizacao = models.ForeignKey(Tipo_ApoioRealizacao, on_delete=CASCADE)

