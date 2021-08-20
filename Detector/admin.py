from django.contrib import admin
from .models import *

class SucursalAdmin(admin.ModelAdmin):
    list_display = ['nombre','propietario','capacidadMaxima',]

class SensorAdmin(admin.ModelAdmin):
    list_display = ['id','nombre',]

class LocalizacionAdmin(admin.ModelAdmin):
    list_display = ['provincia','calle','numero',]

class EntradaAdmin(admin.ModelAdmin):
    list_display = ['hora_entrada', 'sucursal',]

class SalidaAdmin(admin.ModelAdmin):
    list_display = ['hora_salida', 'sucursal']




# Register your models here.
admin.site.register(Localizacion, LocalizacionAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Salida, SalidaAdmin)
admin.site.register(Entrada, EntradaAdmin)