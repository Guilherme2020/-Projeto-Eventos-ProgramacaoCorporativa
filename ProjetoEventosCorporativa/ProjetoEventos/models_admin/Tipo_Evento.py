from django.contrib import admin

from models import Tipo_Evento

class Tipo_Evento_admin(admin.ModelAdmin):
    pass

admin.site.register(Tipo_Evento, TipoEventoModelAdmin)