from django.contrib import admin

from models import Item_inscricao

class Item_Inscricao_admin(admin.ModelAdmin):
	pass
    
admin.site.register(Item_inscricao, ItemInscricaoModelAdmin)