from django.db import models

import Atividade, Evento, Inscricao,Cupom

class Item_Inscricao(models.Model):
    inscricao_cod = models.ForeignKey(Inscricao,on_delete = models.CASCADE)
    atividade_cod = models.ForeignKey(Atividade,on_delete=models.CASCADE)