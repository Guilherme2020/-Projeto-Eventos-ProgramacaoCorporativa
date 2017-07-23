from django.contrib import admin

from models import Atividade

class Atividade_admin(admin.ModelAdmin):
    pass

admin.site.register(Atividade, AtividadeModelAdmin)