from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from biblioteca.models import Culturas
from .models import Batalla, EstadisticasJugador
import random

@login_required
def menu_juego(request):
    """Menú principal del juego"""
    civilizaciones = Culturas.objects.all()
    
    # Obtener o crear estadísticas del jugador
    estadisticas, created = EstadisticasJugador.objects.get_or_create(jugador=request.user)
    
    # Últimas 5 batallas del jugador
    ultimas_batallas = Batalla.objects.filter(jugador=request.user)[:5]
    
    contexto = {
        'civilizaciones': civilizaciones,
        'estadisticas': estadisticas,
        'ultimas_batallas': ultimas_batallas
    }
    
    return render(request, 'juego/menu_juego.html', contexto)


@login_required
def iniciar_batalla(request):
    """Iniciar una batalla"""
    if request.method == 'POST':
        civilizacion_id = request.POST.get('civilizacion_id')
        
        if not civilizacion_id:
            messages.error(request, 'Debes seleccionar una civilización')
            return redirect('menu_juego')
        
        # Obtener civilización del jugador
        civilizacion_jugador = Culturas.objects.get(id=civilizacion_id)
        
        # Seleccionar civilización rival aleatoria (diferente a la del jugador)
        civilizaciones_disponibles = Culturas.objects.exclude(id=civilizacion_id)
        
        if not civilizaciones_disponibles.exists():
            messages.error(request, 'No hay civilizaciones rivales disponibles')
            return redirect('menu_juego')
        
        civilizacion_rival = random.choice(civilizaciones_disponibles)
        
        # Calcular resultado de la batalla
        resultado = calcular_batalla(civilizacion_jugador, civilizacion_rival)
        
        # Guardar batalla
        batalla = Batalla.objects.create(
            jugador=request.user,
            civilizacion_jugador=civilizacion_jugador,
            civilizacion_rival=civilizacion_rival,
            resultado=resultado
        )
        
        # Actualizar estadísticas
        estadisticas, created = EstadisticasJugador.objects.get_or_create(jugador=request.user)
        
        if resultado == 'victoria':
            estadisticas.victorias += 1
            estadisticas.puntos += 10
        elif resultado == 'derrota':
            estadisticas.derrotas += 1
            estadisticas.puntos -= 5
        else:
            estadisticas.empates += 1
            estadisticas.puntos += 3
        
        estadisticas.save()
        
        # Redirigir a resultado
        return redirect('resultado_batalla', batalla_id=batalla.id)
    
    return redirect('resultado_batalla', batalla_id=batalla.id)



def calcular_batalla(civilizacion_jugador, civilizacion_rival):
    """
    Calcula el resultado de la batalla basándose en las características
    """
    # Sistema de puntuación basado en longitud de texto (puedes mejorarlo)
    puntos_jugador = 0
    puntos_rival = 0
    
    # Puntos por fortaleza
    puntos_jugador += len(civilizacion_jugador.fortaleza) * 2
    puntos_rival += len(civilizacion_rival.fortaleza) * 2
    
    # Puntos por bonificación
    puntos_jugador += len(civilizacion_jugador.bonificacion) * 3
    puntos_rival += len(civilizacion_rival.bonificacion) * 3
    
    # Puntos por unidad especial
    puntos_jugador += len(civilizacion_jugador.unidad_especial) * 1.5
    puntos_rival += len(civilizacion_rival.unidad_especial) * 1.5
    
    # Factor aleatorio (suerte)
    puntos_jugador += random.randint(1, 50)
    puntos_rival += random.randint(1, 50)
    
    # Determinar ganador
    diferencia = puntos_jugador - puntos_rival
    
    if diferencia > 20:
        return 'victoria'
    elif diferencia < -20:
        return 'derrota'
    else:
        return 'empate'


@login_required
def resultado_batalla(request, batalla_id):
    """Mostrar resultado de la batalla"""
    batalla = Batalla.objects.get(id=batalla_id, jugador=request.user)
    estadisticas = EstadisticasJugador.objects.get(jugador=request.user)
    
    contexto = {
        'batalla': batalla,
        'estadisticas': estadisticas
    }
    
    return render(request, 'juego/resultado_batalla.html', contexto)


@login_required
def ranking(request):
    """Mostrar ranking de jugadores"""
    ranking_jugadores = EstadisticasJugador.objects.all().order_by('-puntos', '-victorias')[:10]
    
    contexto = {
        'ranking': ranking_jugadores
    }
    
    return render(request, 'juego/ranking.html', contexto)
