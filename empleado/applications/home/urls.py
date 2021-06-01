from django.contrib import admin
from django.urls import path
from . import views

app_name="home_app" 

urlpatterns=[
    path(
        'panel/',
        views.HomePage.as_view(),
        name='panel',
    ),

    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
    ),
    
    path(
        'servicios/',
        views.ServiciosView.as_view(),
        name='servicios'
    ),
    path(
        'equipo/',
        views.EquipoView.as_view(),
        name='equipo'
    ),
    path(
        'contactanos/',
        views.ContactanosView.as_view(),
        name='contactanos'
    ),
    path(
        'ingresar/',
        views.IngresarView.as_view(),
        name='ingresar'
    ),
    path('prueba/',views.PruebaView.as_view()),
    path('lista/',views.PruebaListView.as_view()),
    path('lista-prueba/',views.ListarPrueba.as_view()),
    path('add/',views.PruebaCreateView.as_view(),name='prueba_add'),
    #submétodo as_view: indica que estamos ejecut una vista genérica
    path(
        'resume-foundation/',
        views.ResumeFoundationView.as_view(),
        name='resume_foundation'
    ),
]
