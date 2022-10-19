from django.urls import re_path as path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about, name='home-about'),
    path('classes/', views.classes, name='home-classes')
]
