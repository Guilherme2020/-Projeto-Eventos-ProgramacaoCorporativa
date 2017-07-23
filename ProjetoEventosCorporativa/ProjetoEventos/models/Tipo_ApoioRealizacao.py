from django.db import models
from enum import Enum

import Evento

class TipoApoioChoice(Enum):
	APOIO = 0
	REALIZACAO = 1

class Tipo_ApoioRealizacao(models.Model):
	tipo = EnumField(TipoApoioChoice, max_lenght = 1)