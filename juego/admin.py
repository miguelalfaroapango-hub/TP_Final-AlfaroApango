from django.contrib import admin
from .models import Batalla, EstadisticasJugador

@admin.register(Batalla)
class BatallaAdmin(admin.ModelAdmin):
    list_display = ['jugador', 'civilizacion_jugador', 'civilizacion_rival', 'resultado', 'fecha']
    list_filter = ['resultado', 'fecha']
    search_fields = ['jugador__username', 'civilizacion_jugador__nombre', 'civilizacion_rival__nombre']

@admin.register(EstadisticasJugador)
class EstadisticasJugadorAdmin(admin.ModelAdmin):
    list_display = ['jugador', 'victorias', 'derrotas', 'empates', 'puntos', 'total_batallas']
    search_fields = ['jugador__username']
