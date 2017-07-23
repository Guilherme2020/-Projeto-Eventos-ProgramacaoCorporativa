from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    cadastrarEvento():
    	pass

    inscreverEmEveto():
    	pass

    criarAtividade():
    	pass
