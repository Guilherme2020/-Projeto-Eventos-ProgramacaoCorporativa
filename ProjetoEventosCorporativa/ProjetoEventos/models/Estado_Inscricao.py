from django.db import models
from enum import Enum

import Evento

class EstadoInscricaoChoice(Enum):
	PAGO = 0
	NAOPAGO = 1

class Estado_Inscricao(models.Model):
	estado = EnumField(EstadoInscricaoChoice, max_lenght = 1)