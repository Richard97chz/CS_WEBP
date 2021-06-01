from django.db import models
#
from applications.departamento.models import departamento 
from applications.users.models import User
#importo tabla.no en departamento,por ello voy a la ruta.
from ckeditor.fields import RichTextField

class Habilidades(models.Model):    #cada empleado va a tener un conjunto de habilidades
    habilidad = models.CharField('Habilidad', max_length=50)    #mc: charfield de habilidades

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidadess Empleados'

    def __str__(self):
        return str(self.id)+'-'+self.habilidad  #retorne algo para que modelo esté commpleto

# Create your models here.
class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES=(    #especifico solo valores que puede tener el campo REGISTRO.
        ('0','CONTADOR'),      #en mi BD se guarda la primera columna
        ('1','ADMINISTRADOR'),  #ahorro espacio, pues guardo cadenas de 1 caracter.
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField(   #concatenar nombre y apellido
        'Nombres completos',
        max_length=120,
        blank=True  #decimos que no es obligatorio
    )               #para ver que esta correcto.hacemos la migración

    job = models.CharField('trabajo', max_length=50,choices=JOB_CHOICES)
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE) #creamos la relac.
    
    #User = models.ForeignKey(User, on_delete=models.CASCADE) #creamos la 2da relac.

    avatar = models.ImageField(upload_to='empleado', blank=True,null=True) 
                                        #almacena en empleado lo cual lo bussca en carpeta raiz
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida=RichTextField()

    def __str__(self):
        return str(self.id)+'-'+self.first_name+'-'+self.last_name
    