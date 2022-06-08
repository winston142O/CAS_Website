from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about, name='home-about'),
    path('classes/', views.classes, name='home-classes')
]
