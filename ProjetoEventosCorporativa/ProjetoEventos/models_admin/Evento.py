from django.contrib import admin

from models import Evento

class Evento_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Evento, EventoModelAdmin)