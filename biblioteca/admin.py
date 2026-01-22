from django.contrib import admin
from biblioteca.models import Culturas, estretegias, naval, AcercaDeMi

#admin.site.register(Culturas)

@admin.register(Culturas)
class CulturasAdmin(admin.ModelAdmin):
    #columnas visibles en la lista del modelo
    list_display = ("nombre","unidad_especial","unidad","bonificacion","fortaleza","debilidades")
    #campos para buscar
    search_fields = ("unidad_especial",)
    #orden por defecto 
    ordering = ("unidad_especial","nombre")

@admin.register(naval)
class navalAdmin(admin.ModelAdmin):
    #columnas visibles en la lista del modelo
    list_display = ("unidad","no_unidades","civilizacion","descripcion")
    #campos para buscar
    search_fields = ("civilizacion",)
    #orden por defecto 
    ordering = ("no_unidades","unidad")

@admin.register(estretegias)
class estretegiasAdmin(admin.ModelAdmin):
#columnas visibles en la lista del modelo
    list_display = ("ruta",)

@admin.register(AcercaDeMi)
class AcercaDeMiAdmin(admin.ModelAdmin):
    fields = ['contenido']
    
    def has_add_permission(self, request):
        return not AcercaDeMi.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    

