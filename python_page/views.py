from django.shortcuts import render

# Create your views here.

def python_page(request):
    return render(request, 'python_page/python_themes.html')

def python_installation(request):
    return render(request, 'python_page/installation.html', {'title': 'python-installation'})

def python_default_idle(request):
    return render(request, 'python_page/pythonidle.html', {'title': 'python-defaultidle'})

def python_math_ops(request):
    return render(request, 'python_page/python_math_ops.html', {'title': 'python-mathops'})

def python_intro(request):
    return render(request, 'python_page/python_intro.html', {'title': 'python-intro'})

def python_fluent_tools(request):
    return render(request, 'python_page/python_fluent-tools.html', {'title': 'python-intro'})

def python_data_estructures(request):
    return render(request, 'python_page/python_data_structures.html', {'title': 'python-datastructures'})

def python_modules(request):
    return render(request, 'python_page/python_modules.html', {'title': 'python-modules'})

def python_input_and_output(request):
    return render(request, 'python_page/python_input_and_output.html', {'title': 'python-inputandoutput'})

def python_errors_and_exceptions(request):
    return render(request, 'python_page/python_errors_and_exceptions.html', {'title': 'python-errorsandexceptions'})

def python_classes(request):
    return render(request, 'python_page/python_classes.html', {'title': 'python-classes'})

def python_standard_library(request):
    return render(request, 'python_page/python_standard_library.html', {'title': 'python-standardlibrary'})

def python_standard_library_pt2(request):
    return render(request, 'python_page/python_standard_library_pt2.html', {'title': 'python-standardlibrary2'})

def python_virtual_environments(request):
    return render(request, 'python_page/python_virtual_environments.html', {'title': 'python-venvs'})
    
def python_nowhat(request):
    return render(request, 'python_page/python_nowhat.html', {'title': 'python-nowhat'})
    
def python_interactive_inputs(request):
    return render(request, 'python_page/python_interactive_input.html', {'title': 'python-interactiveinputs'})

def python_arithmetics(request):
    return render(request, 'python_page/python_arithmetics.html', {'title': 'python-arithmetics'})

def python_apendice(request):
    return render(request, 'python_page/python_apendice.html', {'title': 'python-apendice'})