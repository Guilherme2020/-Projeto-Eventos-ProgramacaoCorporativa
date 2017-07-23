from django.contrib import admin

from models import Inscricao

class Inscricao_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Inscricao, InscricaoModelAdmin)