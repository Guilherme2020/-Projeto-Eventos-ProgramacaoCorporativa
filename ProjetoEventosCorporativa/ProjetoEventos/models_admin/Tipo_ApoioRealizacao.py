from django.contrib import admin

from models import Tipo_ApoioRealizacao

class Tipo_Apoio_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Tipo_ApoioRealizacao, TipoApoioRealizacaoModelAdmin)