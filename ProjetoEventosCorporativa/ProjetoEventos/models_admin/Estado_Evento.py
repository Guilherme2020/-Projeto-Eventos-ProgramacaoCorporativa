from django.contrib import admin

from models import Estado_Evento

class Estado_Evento_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Estado_Evento, EstadoEventoModelAdmin)