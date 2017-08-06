# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

class Instituicao(models.Model):
    nome = models.CharField(max_length=45)
    local_instituicao = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    
class Estado_Evento(models.Model):
	EVENTO_TYPE_CHOICES = (
    ('0', 'ABERTO'),
    ('1', 'EM ANDAMENTO'),
    ('2', 'ENCERRADO'),
	)
	estado = models.CharField(max_length=1, choices=EVENTO_TYPE_CHOICES)
	
class Tipo_Evento(models.Model):
	TIPO_EVENTO_TYPE_CHOICES = (
    ('0', 'SIMPOSIO'),
    ('1', 'CONGRESSO'),
    ('2', 'JORNADA'),
    ('3', 'SEMANACIENTIFICA'),
    ('4', 'CICLODEPALESTRA'),
	)
	tipo = models.CharField(max_length=1, choices=TIPO_EVENTO_TYPE_CHOICES)

class Evento(models.Model):
    evento_cod = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)
    tipo_evento = models.ForeignKey(Tipo_Evento, on_delete = models.CASCADE)
    estado_evento = models.ForeignKey(Estado_Evento, on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()

class Cupom(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    cod_cupom = models.CharField(max_length=45)
    desconto = models.IntegerField()
    data_validade = models.DateField()


class Tipo_ApoioRealizacao(models.Model):
	APOIO_TYPE_CHOICES = (
    ('0', 'APOIO'),
    ('1', 'REALIZACAO'),
	)
	tipo = models.CharField(max_length=1, choices=APOIO_TYPE_CHOICES)

class Apoio_Realizacao(models.Model):
    cod_apoio = models.CharField(max_length=5)
    instituicao_cod = models.ForeignKey(Instituicao,on_delete=models.CASCADE)
    evento_cod = models.ForeignKey(Evento,on_delete=models.CASCADE)
    tipo_ApoioRealizacao = models.ForeignKey(Tipo_ApoioRealizacao, on_delete=models.CASCADE)

class Tipo_Atividade(models.Model):
	ATIVIDADE_TYPE_CHOICES = (
    ('0', 'PALESTRA'),
    ('1', 'MINICURSO'),
    ('2', 'MESAREDONDA'),
	)
	tipo = models.CharField(max_length=1, choices=ATIVIDADE_TYPE_CHOICES)

class Atividade(models.Model):
    nome = models.CharField(max_length=45)
    tipoAtividade = models.ForeignKey(Tipo_Atividade, on_delete = models.CASCADE)
    evento_cod_evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    valor = models.FloatField()
    
class Estado_Inscricao(models.Model):
	INSCRICAO_TYPE_CHOICES = (
    ('0', 'PAGO'),
    ('1', 'NAOPAGO'),
	)
	estado = models.CharField(max_length=1, choices=INSCRICAO_TYPE_CHOICES)


class Inscricao(models.Model):
    usuario_cod = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_inscricao = models.DateField()
    valor_total = models.FloatField()
    evento_cod = models.ForeignKey(Evento, on_delete=models.CASCADE)
    pagamento = models.DateField()
    estado = models.ForeignKey(Estado_Inscricao, on_delete=models.CASCADE)


class Item_Inscricao(models.Model):
    inscricao_cod = models.ForeignKey(Inscricao,on_delete = models.CASCADE)
    atividade_cod = models.ForeignKey(Atividade,on_delete=models.CASCADE)


