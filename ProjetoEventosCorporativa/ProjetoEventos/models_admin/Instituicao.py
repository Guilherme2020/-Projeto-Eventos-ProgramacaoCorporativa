from django.contrib import admin

from models import Instituicao

class Instituicao_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Instituicao, InstituicaoModelAdmin)