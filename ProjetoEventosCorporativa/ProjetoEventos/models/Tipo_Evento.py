from django.db import models
from enum import Enum

class TipoEventoChoice(Enum):
	SIMPOSIO = 0
	CONGRESSO = 1
	JORNADA = 2
	SEMANACIENTIFICA = 3
	CICLODEPALESTRA = 4

class Tipo_Evento(models.Model):
	tipo = EnumField(TipoEventoChoice, max_lenght = 1)