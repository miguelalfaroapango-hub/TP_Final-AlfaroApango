from django.db import models
from django.conf import settings
from biblioteca.models import Culturas

class Batalla(models.Model):
    # Usuario que juega - ACTUALIZADO para usar el modelo personalizado
    jugador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='batallas')
    
    # Civilizaciones en batalla
    civilizacion_jugador = models.ForeignKey(Culturas, on_delete=models.CASCADE, related_name='batallas_como_jugador')
    civilizacion_rival = models.ForeignKey(Culturas, on_delete=models.CASCADE, related_name='batallas_como_rival')
    
    # Resultado
    RESULTADO_CHOICES = [
        ('victoria', 'Victoria'),
        ('derrota', 'Derrota'),
        ('empate', 'Empate'),
    ]
    resultado = models.CharField(max_length=10, choices=RESULTADO_CHOICES)
    
    # Fecha de la batalla
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.jugador.username} - {self.civilizacion_jugador.nombre} vs {self.civilizacion_rival.nombre} ({self.resultado})"
    
    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Batalla'
        verbose_name_plural = 'Batallas'


class EstadisticasJugador(models.Model):
    jugador = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='estadisticas')
    
    # Contadores
    victorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)
    
    # Puntuación
    puntos = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Estadísticas de {self.jugador.username}"
    
    @property
    def total_batallas(self):
        return self.victorias + self.derrotas + self.empates
    
    @property
    def porcentaje_victorias(self):
        if self.total_batallas == 0:
            return 0
        return round((self.victorias / self.total_batallas) * 100, 2)
