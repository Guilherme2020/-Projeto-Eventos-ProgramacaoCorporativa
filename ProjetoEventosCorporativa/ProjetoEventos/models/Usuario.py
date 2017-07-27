<<<<<<< HEAD


from django.db import models


class Usuario(models.Model):
    cod_user = models.IntegerField()
=======
from django.db import models

class Usuario(models.Model):
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

<<<<<<< HEAD


=======
    cadastrarEvento():
    	pass

    inscreverEmEveto():
    	pass

    criarAtividade():
    	pass
>>>>>>> 342be8ee61a29c4d836d352fef99b4490bbee3d5
