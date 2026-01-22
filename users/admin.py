from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('avatar', 'pais', 'direccion')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'pais', 'is_staff']
