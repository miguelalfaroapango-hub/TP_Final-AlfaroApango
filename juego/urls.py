from django.urls import path
from juego.views import *

urlpatterns = [
    path('', menu_juego, name='menu_juego'),
    path('iniciar_batalla/', iniciar_batalla, name='iniciar_batalla'),
    path('resultado/<int:batalla_id>/', resultado_batalla, name='resultado_batalla'),
    path('ranking/', ranking, name='ranking'),
]
