from django.db import models

class Culturas(models.Model):
    nombre = models.CharField(max_length=50)
    unidad_especial = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    bonificacion = models.CharField(max_length=150)
    fortaleza = models.CharField(max_length=100)
    debilidades = models.CharField(max_length=100)

    def __str__(self):
        return f"Nombre: {self.nombre} / unidad_especial: {self.unidad_especial}"   

class naval(models.Model):
    unidad = models.CharField(max_length=50)
    no_unidades =models.IntegerField(null=False) #pones un numero y evitas el cero 
    #campos para buscar
    civilizacion = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return f"unidad: {self.unidad} / no_unidades: {self.no_unidades}"  
    
class estretegias(models.Model):
    ruta = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f"ruta: {self.ruta} "  
    
class AcercaDeMi(models.Model):
    contenido = models.TextField(
        default="Escribe aquí tu información personal...",
        help_text="Contenido de la página Acerca de Mí"
    )
    
    # Para asegurar que solo haya un registro
    def save(self, *args, **kwargs):
        self.pk = 1
        super(AcercaDeMi, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        pass
    
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def __str__(self):
        return "Información de Acerca de Mí"
    
    class Meta:
        verbose_name = "Acerca de Mí"
        verbose_name_plural = "Acerca de Mí"
