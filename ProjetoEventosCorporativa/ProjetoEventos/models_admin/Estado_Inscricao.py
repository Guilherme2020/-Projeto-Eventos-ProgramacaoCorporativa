from django.contrib import admin

from models import Estado_Inscricao

class Estado_Inscricao_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Estado_Inscricao, EstadoInscricaoModelAdmin)