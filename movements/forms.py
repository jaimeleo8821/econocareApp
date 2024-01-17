from django import forms
from django.core import validators
from .models import Category, Type, Pay_Method, Movement


class FormType(forms.Form):
    
    movement_type = forms.CharField(
        label = "Tipo de Movimiento",
        max_length=40, 
        required=True,
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(3,'El nombre del Tipo de movimiento es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ÑñÁÉÍÓÚáéíóú]*$','El nombre del tipo de movimiento esta mal formado','invalid_name')
        ]
    )

    movement_type.widget.attrs.update({
        'placeholder':'Escriba un nombre para el tipo de movimiento'
    })

class FormCategory(forms.Form):

    type = forms.IntegerField(
        label = "Tipo de Movimiento", # type: ignore
        widget=forms.NumberInput()
    )
    type.widget.attrs.update({
        'placeholder':'Código del tipo de movimiento'
    })

    category = forms.CharField(
        label = "Categoría del Movimiento",
        max_length=40, 
        required=True,
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(3,'El nombre de la Categoría del movimiento es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ÑñÁÉÍÓÚáéíóú]*$','El nombre de la Categoría del movimiento esta mal formado','invalid_name')
        ]
    )    
    category.widget.attrs.update({
        'placeholder':'Escriba un nombre para la cateoría del movimiento'
    })

class FormPayMethod(forms.Form):

    pay_method = forms.CharField(
        label="Método de Pago",
        max_length=40, 
        required=True,
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(3,'El nombre del Método de Pago es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ÑñÁÉÍÓÚáéíóú]*$','El nombre del Método de Pago esta mal formado','invalid_name')
        ]
    )
    pay_method.widget.attrs.update({
        'placeholder':'Escriba un nombre para método de pago'
    })