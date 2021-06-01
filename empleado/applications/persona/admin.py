from django.contrib import admin

from .models import Empleado, Habilidades
# Register your models here.
#admin.site.register(Empleado)
admin.site.register(Habilidades)

class EmpleadoAdmin (admin.ModelAdmin): #ModelAdmin: heredo este atributo que ya existe dentro de DJ
    list_display=(
        'first_name',
        'last_name',                #Quiero que me retorne estos
        'departamento',
        #'User',
        'job',
        'full_name',    #Agregamos, este no existe dentro de mis modelos
        'id',   #q me muestre el atributo ID
    )
    #------------
    def full_name(self,obj): #creo función. con list_display solo puedo llamar a atributos que existe en mi modelo.
        #toda la operación
        print(obj.first_name)
        return obj.first_name+' '+obj.last_name
    #------------
    search_fields=('first_name',) #otro parámetro.Indico en base a qué atributo hacer la búsqueda.
    list_filter=('departamento','job','habilidades') #Para hacer filtro necesito una tupla, por eso se pone la coma
    #
    filter_horizontal=('habilidades',) #solo funciona para campos m2m, que en nuestro caso son habilidades.
admin.site.register(Empleado, EmpleadoAdmin)  #conecto al poner el mismo nombre del class