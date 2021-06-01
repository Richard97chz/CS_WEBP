from django.shortcuts import render

# Create your views here.
#from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView
)
# Import models
from .models import Prueba 
from .forms import PruebaForm  #para el model form parte1


class HomePage(TemplateView): #agregado
    template_name='home/index.html'

class InicioView(TemplateView):
    template_name='iniciohome.html'
'''
class NosotrosView(TemplateView):
    template_name='home/nosotroshome.html'
'''
class ServiciosView(TemplateView):
    template_name='home/servicioshome.html'

class EquipoView(TemplateView):
    template_name='home/equipohome.html'

class ContactanosView(TemplateView):
    template_name='home/contactanoshome.html'

class IngresarView(TemplateView):
    template_name='home/ingresarhome.html'

class PruebaView(TemplateView):
    template_name='home/prueba.html'

class ResumeFoundationView(TemplateView):
    template_name='home/resume_foundation.html'


class PruebaListView(ListView):     #PruebaListVies es una lista genérica
    template_name = 'home/lista.html'
    context_object_name='listaNumeros'
    queryset=['5','10','15']     #no solo pueden ser así, sino registros de una BD.


class ListarPrueba(ListView):   #El listview heredo de la vista genérica. 
                                #interpreta que quiero listar todo o que tenga el modelo prueba. 
    template_name = "home/lista_prueba.html"  #ubicación
    model=Prueba
    context_object_name='lista'  #accedemos al resultado de listar de tabla prueba.


class PruebaCreateView(CreateView):         #formulario
    template_name = "home/add.html"
    model=Prueba
    #fields=['titulo','subtitulo','cantidad']
    form_class=PruebaForm
    success_url='/' #Al copletarse el proceso va a la pagina principal o de inicio 

    
