from django import forms

from .models import Cliente

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = (
            'nombre',
            'apellidos',
            'profesion',
            'telefono',
            'direccion',
            'ciudad',
            'foto',
        )
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'ingrese nombre'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'ingrese apellidos'}),
            'profesion': forms.TextInput(attrs={'placeholder': 'ingrese profesión'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'ingrese teléfono'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'ingrese dirección'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'ingrese ciudad'})
            }
                   