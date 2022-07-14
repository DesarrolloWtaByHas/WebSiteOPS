from django.contrib import admin
from isla_N.models import PlanesServiciosEspeciales, PlanesMorarbe, PlanesKonecta, PlanesWTA, NumerosAxxaAssistance
# Register your models here.

admin.site.register(PlanesServiciosEspeciales)
admin.site.register(PlanesMorarbe)
admin.site.register(PlanesKonecta)
admin.site.register(PlanesWTA)

class NumerosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono']

admin.site.register(NumerosAxxaAssistance, NumerosAdmin)
