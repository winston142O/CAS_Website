from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import models
from django.db import models
from django.forms.fields import ImageField

from .models import Profile
from django.core import validators
from django.utils.translation import gettext_lazy as _, ngettext_lazy

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label= 'Correo Electrónico',
        required=True,
    )

    username = forms.CharField(
        max_length=40, 
        required=True,
        label='Nombre de Usuario'
    )
    
    first_name = forms.CharField(
        required=True,
        label='Nombre'
    )
    
    last_name = forms.CharField(
        required=True,
        label='Apellido'
    )
    
    password1 = forms.PasswordInput(
    )
    password2 = forms.PasswordInput(
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Correo Electrónico',
        required=True
    )

    username = forms.CharField(
        required=True,
        label='Nombre de Usuario',
    )

    description = forms.CharField(
        label = 'Sobre ti (Máximo 600 caracteres)',
        required=False,
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'description']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label = 'Foto de perfil'
    )
    
    bg_image = forms.ImageField(
        label = 'Banner (Máximo 1080p)'
    )
    
    class Meta:
        model = Profile
        fields = ['image', 'bg_image']

