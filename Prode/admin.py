from django.contrib import admin
from Prode.models import Equipos,Fase,Partido,EquipoPartido,Resultado

# Register your models here.
@admin.register(Equipos)
class equiposAdmin(admin.ModelAdmin):
    list_display = ['descripcion','activo']

@admin.register(Fase)
class faseAdmin(admin.ModelAdmin):
    list_display = ['descripcion','activo']

@admin.register(Partido)
class partidoAdmin(admin.ModelAdmin):
    list_display = ['fase','descripcion','activo','fecha']

@admin.register(EquipoPartido)
class EquipoPartidoAdmin(admin.ModelAdmin):
    list_display = ['partido','equipo']

@admin.register(Resultado)
class resultadoAdmin(admin.ModelAdmin):
    list_display = ['equipo_partido','cant_goles']
