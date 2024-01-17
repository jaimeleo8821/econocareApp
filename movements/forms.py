from django import forms
from django.core import validators
from .models import Category, Type, Pay_Method, Movement


class FormType(forms.Form):
    
    type = forms.CharField(
        label = "Tipo de Movimiento",
        max_length=40, 
        required=True,
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(3,'El nombre del Tipo de movimiento es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ÑñÁÉÍÓÚáéíóú]*$','El nombre del tipo de movimiento esta mal formado','invalid_name')
        ]
    )

    type.widget.attrs.update({
        'placeholder':'Escriba un nombre para el tipo de movimiento'
    })
