from django.db import models
from django.contrib.auth.models import AbstractUser

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class Perfil(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        blank=True,
        null=True,
        verbose_name="Avatar"
    )
    pais = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"{self.username}: {self.first_name}, {self.last_name}"
