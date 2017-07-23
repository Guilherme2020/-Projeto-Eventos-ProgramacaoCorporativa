from django.contrib import admin

from models import Usuario

class Usuario_admin(admin.ModelAdmin):
	pass    

admin.site.register(Usuario)

