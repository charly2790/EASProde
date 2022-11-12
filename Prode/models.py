from django.db import models
from django.utils import timezone

# Create your models here.
class Equipos(models.Model):
    descripcion = models.CharField(null=False,blank=False,max_length=64)
    activo = models.BooleanField(default = True)
    img_bandera = models.ImageField(upload_to = 'imagenes_banderas',default = 'imagenes_banderas/bandera-img-default.png',blank = True,null = True)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

class Fase(models.Model):
    descripcion = models.CharField(null = False, blank = False, max_length = 64)
    activo = models.BooleanField(default = True)

    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"

    def __str__(self):
        return self.descripcion

class Partido(models.Model):
    fase = models.ForeignKey(Fase,on_delete = models.DO_NOTHING)
    descripcion = models.CharField(null = False, blank = False,max_length = 64)
    activo = models.BooleanField(default = True)
    fecha = models.DateField(default = timezone.now)

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
    
    def __str__(self):
        return self.descripcion


class EquipoPartido(models.Model):
    partido = models.ForeignKey(Partido,on_delete = models.DO_NOTHING)
    equipo = models.ForeignKey(Equipos,on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name = "Equipo por partido"
        verbose_name_plural = "Equipos por partido"

    def __str__(self):
        
        desc = f"{self.partido} - {self.equipo}"
        
        return desc

class Resultado(models.Model):
    equipo_partido = models.ForeignKey(EquipoPartido,on_delete = models.DO_NOTHING)
    cant_goles = models.IntegerField(default = 0)

    class Meta:
        verbose_name = "Resultado final"
        verbose_name_plural = "Resultados finales"
