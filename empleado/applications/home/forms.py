#Acá escribiré las personalizaciones para los campos
from django import forms #paquete interno que me ayuda a crear formularios
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model=Prueba
        #fields=('__all__')
        fields=(
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets={
            'titulo':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese texto aquí'
                }
            )
        }
    '''
    def clean_cantidad(self):  #a la altura de class xq estamos escrib un metodo para prueba form
        cantidad = self.cleaned_data['cantidad'] #recupero lo que se escribe en cantidad
        if cantidad<10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')

        return cantidad
    '''