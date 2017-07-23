# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ProjetoEventos.models import Usuario, Tipo_Evento, Item_Inscricao,Inscricao,Evento,Estado_Inscricao,Estado_Evento, Cupom, Atividade, Apoio_Realizacao, Tipo_Atividade, Tipo_ApoioRealizacao

class Usuario_admin(admin.ModelAdmin):
	pass    

admin.site.register(Apoio_Realizacao)
admin.site.register(Atividade)
admin.site.register(Cupom)
admin.site.register(Estado_Evento)
admin.site.register(Estado_Inscricao)
admin.site.register(Evento)
admin.site.register(Inscricao)
admin.site.register(Item_Inscricao)
admin.site.register(Tipo_ApoioRealizacao)
admin.site.register(Tipo_Atividade)
admin.site.register(Tipo_Evento)
admin.site.register(Usuario)
