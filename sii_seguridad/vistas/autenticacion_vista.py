from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from sii_seguridad.formularios.autenticacion_form import LoginForm


def login(request):
    # Carga el form
    if request.method == 'GET':
        return render(request, 'signin.html', {
            "form": AuthenticationForm
        })
    # Autentifica por POST
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'autenticacion/signin.html', {
                "form": AuthenticationForm, 
                "error": "Username or password is incorrect."
            })
        login(request,user)
        return redirect('/dashboard')

@login_required
def signout(request):
    logout_django(request)
    return redirect('/')
