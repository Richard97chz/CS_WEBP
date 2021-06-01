from django.shortcuts import render
from django.urls import reverse_lazy    #para importar un paquete para redireccion
# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

#models
from .models import Empleado
#forms
from .forms import EmpleadoForm
#autentification
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class InicioView(TemplateView):
    """vista que carga la pagina de inicio"""
    template_name='inicio.html'
    
class ListAllEmpleados(ListView):
    template_name='persona/list_all.html'
    paginate_by=4   #tamaño de bloques en que queremos paginar
    ordering='first_name' #ordenar en base al primer nombre
    #model=Empleado
    def get_queryset(self):      #cn esto no será necesario pasarle el parámetro model
        print('***********')
        palabra_clave = self.request.GET.get("kword",'')
        #pedro=pe
        lista=Empleado.objects.filter(
            #first_name=palabra_clave
            first_name__icontains=palabra_clave #busca letra o conj de 2 letras
        )
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name='persona/lista_empleados.html'
    paginate_by=10   #tamaño de bloques en que queremos paginar
    ordering='first_name' #ordenar en base al primer nombre
    context_object_name='empleados'
    model=Empleado
    #Quitamos el query set que servia para hacer filtros



class ListByAreaEmpleado(ListView):
    """lista empleados de una area"""
    template_name='persona/list_by_area.html'
    context_object_name='empleados'
    """queryset=Empleado.objects.filter(
        departamento__shor_name='imp'
    )""" 

    def get_queryset(self): #debe retornar siempre una lista
        #el codigo que quiera
        area=self.kwargs['shorname']
        lista=Empleado.objects.filter(
            departamento__shor_name=area
        )
        return lista

class ListEmpleadosByKword(ListView):
    """lista empleados por palabra clave"""
    template_name='persona/by_kword.html'
    context_object_name='empleados'

    def get_queryset(self): 
        print('*********************')
        palabra_clave=self.request.GET.get("kword",'')  #intercepto solicitudes enviadas al servidor
        #print('=====',palabra_clave)                    #en este caso de tipo GET.
        #return []                                       #y q me recupere el valor cuya identif sea keyword
        lista=Empleado.objects.filter(
            first_name=palabra_clave
        )
        #print('lista resultado:', lista)
        return lista
    
class ListHabilidadesEmpleado(ListView):
    """lista empleados de una area"""
    template_name='persona/habilidades.html'
    context_object_name='habilidades'

    def get_queryset(self): #debe retornar siempre una lista
        #el codigo que quiera
        empleado=Empleado.objects.get(id=10) #me recupera 1 reg de la BD
        #print(empleado.habilidades.all()) #voy a reg emplead, al atrib many2many llamad habilid. y met all
        #return []
        return empleado.habilidades.all() #q me muestre a mi template

class EmpleadoDetailView(DetailView):   #para ver detalle de cada empleado
    model=Empleado  #necesita el parametro modelo
    template_name='persona/detail_empleado.html'  #trabaja con un template(vista basada en clase)

    def get_context_data(self, **kwargs): 
        context=super(EmpleadoDetailView,self).get_context_data(**kwargs)
        #Toot un proceso
        context['titulo']='Empleado del mes'
        return context

class SuccessView(TemplateView):            #d35
    template_name="persona/success.html"

class EmpleadoCreateView(CreateView):
    template_name="persona/add.html"
    model=Empleado
    #fields=['first_name','last_name','job']
    #fields=('__all__')  #trae todo los campos del modelo empleado
    form_class=EmpleadoForm     #configurar y personalizar lso formularios
    '''
    fields=[
        'first_name',   #especificamos solo los atributos queremos se visualien
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
    ]
    '''
    #success_url='.'   #<--si quiero que recargue la misma pagina
    #success_url='/success'          #d35
    success_url=reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form): #almacena el formulario que estamos enviando dsd registrar persona.
        #logica del proceso
        empleado=form.save(commit=False)    #guardar lo que estoy llenando (no es muy optimo)
        empleado.full_name=empleado.first_name+' '+empleado.last_name
        empleado.save()     #para que full_name se refleje en BD
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields=[
        'first_name',  #campos que deseo modificar
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url=reverse_lazy('persona_app:empleados_admin') 
    #nose redirecciona cuando el proceso es completo, le digo que no se vaya a url correcto, sino
    #a empleados_admin que ees la vista desde donde modificamos

    def post(self, request, *args, **kwargs):  #post se ejecutará 1º
        self.object = self.get_object()
        print('**************METODO POST*************')
        print('**************************************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):                 #y luego resien este form_valid
        #logica del proceso
        self.object = self.get_object()
        print('**************METODO form valid*************')
        print('**************************************')
        return super(EmpleadoUpdateView,self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model=Empleado
    template_name="persona/delete.html"
    success_url=reverse_lazy("persona_app:empleados_admin")

'''
def login_request(request):
    form=AuthenticationForm()
    return render(request,"")
'''