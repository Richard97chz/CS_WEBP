from django import forms
#Como vamos a depender de un modelo creamos un modelform
from .models import Empleado

#Escribo: mf
class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )
        widgets={
            'habilidades': forms.CheckboxSelectMultiple()

        }
