from django.shortcuts import render, redirect
from biblioteca.models import Culturas, naval, estretegias, AcercaDeMi
from biblioteca.forms import CulturasForm, RegisterForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # ✅ NUEVO

# ✅ TUS VISTAS EXISTENTES
def home(request):
    return render(request, "biblioteca/index.html")

def listar_civilizaciones(request):
    nombre = request.GET.get("nombre")
    civilizaciones_query = Culturas.objects.all()
    if nombre:
        civilizaciones_query = Culturas.objects.filter(
            nombre__icontains=nombre
        )
    contexto = {
        "civilizaciones": civilizaciones_query
    }
    return render(request, "biblioteca/civilizaciones.html", contexto)

def tropas(request):
    tropas_query = Culturas.objects.all()
    contexto = {
        "tropas": tropas_query
    }
    return render(request, "biblioteca/tropas.html", contexto)

def listar_naval(request):
    unidad = request.GET.get("unidad")
    unidades_navales_query = naval.objects.all()
    
    if unidad:
        unidades_navales_query = naval.objects.filter(
            unidad__icontains=unidad
        )
    
    contexto = {
        "unidades_navales": unidades_navales_query
    }
    return render(request, "biblioteca/naval.html", contexto)

# ✅ VISTA PROTEGIDA - Solo usuarios logueados pueden crear culturas
@login_required
def crear_culturas(request):
    if request.method == "POST":
        form = CulturasForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cultura creada exitosamente!')
            return redirect("civilizaciones_list")
    else:
        form = CulturasForm()
    return render(request, 'biblioteca/crear_culturas.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)  # ✅ Agregamos request.FILES
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido al Imperio, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegisterForm()
    
    return render(request, 'biblioteca/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de vuelta, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'biblioteca/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, '¡Has salido del Imperio!')
    return redirect('home')

def acerca_de_Mi(request):
    info = AcercaDeMi.load()
    contexto = {
        'contenido': info.contenido
    }
    return render(request, 'biblioteca/acerca_de_Mi.html', contexto)

from biblioteca.forms import CulturasForm, RegisterForm, LoginForm, EditarPerfilForm

@login_required
def ver_perfil(request):
    """Ver perfil del usuario"""
    return render(request, 'biblioteca/perfil.html')


@login_required
def editar_perfil(request):
    """Editar perfil del usuario"""
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Perfil actualizado exitosamente!')
            return redirect('ver_perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    
    return render(request, 'biblioteca/editar_perfil.html', {'form': form})
