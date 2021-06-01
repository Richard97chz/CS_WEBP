from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import FormView
from applications.persona.models import Empleado    #si esta en otra app
from .models import departamento
# Create your views here.
from .forms import NewDepartamentoForm      # . si está a la misma altura


class DepartamentoListView(ListView):
    template_name='departamento/lista.html'
    model=departamento  #formulario para que reciba datos
    context_object_name='departamentos' #lo redefinimos para usar el nombre'depart..'  en html.

#class NewDepartamentoView(FormView):
class NewDepartamentoView(FormView):
    
    template_name='departamento/new_departamento.html'
    form_class=NewDepartamentoForm  #formulario para que reciba datos
    success_url='/'

    def form_valid(self,form):
        print('*******estamos en el form  valid****')
        
        depa=departamento(          #instancia del modelo departamento
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']
        )
        depa.save()     #para guardar en la BD
        
        nombre=form.cleaned_data['nombre']
        apellido=form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        
        return super(NewDepartamentoView,self).form_valid(form)