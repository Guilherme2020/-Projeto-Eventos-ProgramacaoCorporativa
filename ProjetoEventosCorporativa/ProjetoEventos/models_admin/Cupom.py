from django.contrib import admin

from models import Cupom

class Cupom_admin(admin.ModelAdmin):
	pass

admin.site.register(Cupom, CupomModelAdmin)