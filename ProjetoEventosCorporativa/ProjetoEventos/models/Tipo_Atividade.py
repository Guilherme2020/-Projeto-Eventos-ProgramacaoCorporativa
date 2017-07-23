from django.db import models
from enum import Enum

import Evento

class TipoAtividadeChoice(Enum):
	PALESTRA = 0
	MINICURSO = 1
	MESAREDONDA = 2

class Tipo_Atividade(models.Model):
	tipo = EnumField(TipoAtividadeChoice, max_lenght = 1)