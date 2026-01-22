from django.urls import path
from biblioteca.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URLs existentes
    path("", home, name="home"),
    path("Lista_civilizaciones", listar_civilizaciones, name="civilizaciones_list"),
    path("tropas", tropas, name="tropas"),
    path("crear_cultu", crear_culturas, name="crear_culturas"),
    path("naval", listar_naval, name="naval_list"),
    
    # URLs de autenticación
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    
    # URLs de recuperación de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='biblioteca/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='biblioteca/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='biblioteca/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='biblioteca/password_reset_complete.html'), name='password_reset_complete'),
    
    # URLs de informacion general 
    path("acerca_de_Mi/", acerca_de_Mi, name="acerca_de_Mi"),

    # URLs de edicion
    path("perfil/", ver_perfil, name="ver_perfil"),
path("perfil/editar/", editar_perfil, name="editar_perfil"),




]
