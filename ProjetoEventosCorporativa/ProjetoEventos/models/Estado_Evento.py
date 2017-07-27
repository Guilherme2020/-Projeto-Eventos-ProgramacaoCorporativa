from django.db import models
from enum import Enum

class EstadoEstadoEvento(Enum):
	ABERTO = 0
	EMANDAMENTO = 1
	ENCERRADO = 2

class Estado_Evento(models.Model):
	estado = EnumField(EstadoEstadoEvento, max_lenght = 1)
