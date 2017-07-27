from django.contrib import admin

from models import Tipo_Atividade

class Tipo_Atividade_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Tipo_Atividade, TipoAtividadeModelAdmin)