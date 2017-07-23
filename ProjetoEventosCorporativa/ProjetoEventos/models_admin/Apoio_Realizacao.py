from django.contrib import admin

from models import Apoio_Realizacao

class Apoio_Realizacao_admin(admin.ModelAdmin):
    pass

admin.site.register(Apoio_Realizacao, HospitalModelAdmin)
