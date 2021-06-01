from django.db import models
# Create your models here.
class departamento (models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)  #especificamos cantidad razonable
    shor_name=models.CharField('Nombre Corto',max_length=20) #CharField: usaremos la ORM de DJ
    anulate = models.BooleanField('Anulado',default=False) #si no especificamos,el valor del anulate,DJ le pondrá FALSO.

    class Meta:
        verbose_name='Mi departamento'  #Nombre de nuestro modelo
        verbose_name_plural='Areas de la empresa'   #Nombre que indic. a DJ que tenga cuando quiera mostrarlo en plural
        ordering=['-name']  #ordenar departamentos listado: name:orden alfab. -name: orden inverso
        unique_together=('name','shor_name') #no permite que se registre un atributo 2 veces o combinación de ellas.

        #TAREA: HACER LO MISMO PARA APP PERSONA.

    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.shor_name