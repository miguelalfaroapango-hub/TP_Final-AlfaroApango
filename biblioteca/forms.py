from django import forms
from biblioteca.models import Culturas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import Perfil

# ✅ Formulario de Culturas
class CulturasForm(forms.ModelForm):
    class Meta:
        model = Culturas
        fields = [
            "nombre",
            "unidad_especial",
            "unidad",
            "fortaleza",
            "bonificacion",
            "debilidades",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad_especial': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fortaleza': forms.Textarea(attrs={'class': 'form-control'}),
            'bonificacion': forms.Textarea(attrs={'class': 'form-control'}),
            'debilidades': forms.Textarea(attrs={'class': 'form-control'})
        }

# ✅ Formulario de Registro
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Correo del Guerrero'
        })
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Nombre'
        })
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Apellido'
        })
    )
    pais = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'País'
        })
    )
    direccion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Dirección'
        })
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control medieval-input',
            'accept': 'image/*'
        })
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Contraseña Secreta'
        })
    )
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Confirma tu Contraseña'
        })
    )

    class Meta:
        model = Perfil
        fields = ['username', 'email', 'first_name', 'last_name', 'pais', 'direccion', 'avatar', 'password1', 'password2']


# ✅ Formulario de Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Nombre del Guerrero'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Contraseña'
        })
    )
class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Nombre'
        })
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Apellido'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Correo'
        })
    )
    pais = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'País'
        })
    )
    direccion = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control medieval-input',
            'placeholder': 'Dirección'
        })
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control medieval-input',
            'accept': 'image/*'
        })
    )
    
    class Meta:
        model = Perfil
        fields = ['first_name', 'last_name', 'email', 'pais', 'direccion', 'avatar']
