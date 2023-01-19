from django.urls import path

from sii_seguridad.vistas.autenticacion_vista import login, signout

urlpatterns = [
    path('signin/', login),
    path('logout/', signout),
]
