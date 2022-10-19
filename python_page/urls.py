from django.urls import re_path as path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.python_page, name='getting-started'),
    path('py-installation/', views.python_installation, name='python-installation'),
    path('py-defaultidle/', views.python_default_idle, name='python-defaultidle'),
    path('py-mathops/', views.python_math_ops, name='python-mathops'),
    path('py-intro/', views.python_intro, name='python-intro'),
    path('py-fluent-tools/', views.python_fluent_tools, name='python-fluent-tools'),
    path('py-data-structures/', views.python_data_estructures, name='python-data-structures'),  
    path('py-modules/', views.python_modules, name='python-modules'),                              
    path('py-input-and-output/', views.python_input_and_output, name='python-input-output'),                       
    path('py-errors-and-exceptions/', views.python_errors_and_exceptions, name='python-errors-and-exceptions'),                       
    path('py-classes/', views.python_classes, name='python-classes'),                       
    path('py-standard-library/', views.python_standard_library, name='python-standard-library'),                       
    path('py-standard-library_pt2/', views.python_standard_library_pt2, name='python-standard-library_pt2'),                       
    path('py-virtual-environments/', views.python_virtual_environments, name='python-venvs'),                       
    path('py-now-what/', views.python_nowhat, name='python-nowhat'),                       
    path('py-interactive-inputs/', views.python_interactive_inputs, name='python-interactive-inputs'),   
    path('py-arithmetics/', views.python_arithmetics, name='python-arithmetics'),      
    path('py-apendice/', views.python_apendice, name='python-apendice')         
]


