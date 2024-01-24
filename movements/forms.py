from django import forms
from django.core import validators
from .models import Category, Type, Pay_Method, Origin


class TypeForm(forms.Form):

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

    class Meta:
        model = Type
        fields = ('type',)

class OriginForm(forms.Form):
    
    origin = forms.CharField(
        label = "Origen del Movimiento",
        max_length=40, 
        required=True,
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(3,'El nombre del Origen del movimiento es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ÑñÁÉÍÓÚáéíóú]*$','El nombre del Origen del Movimiento esta mal formado','invalid_name')
        ]
    )

    origin.widget.attrs.update({
        'placeholder':'Escriba un nombre para el Origen del movimiento'
    })

class CategoryForm(forms.Form):

    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        label = "Tipo de movimiento",
        to_field_name="id"
    )
        
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
        'placeholder':'Escriba un nombre para la categoría del movimiento'
    })

class PayMethodForm(forms.Form):

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

class MovementForm(forms.Form):

    idOrigin = forms.ModelChoiceField(
        queryset=Origin.objects.all(),
        label="Origen del movimiento",
        to_field_name="id"
    )
    idType = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        label="Tipo de movimiento",
        to_field_name="id"
    )
    idCategory = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoría del movimiento",
        to_field_name="id"
    )
    idPayMethod = forms.ModelChoiceField(
        queryset=Pay_Method.objects.all(),
        label="Método de Pago",
        to_field_name="id"
    )
    amount = forms.DecimalField(
        label="Valor",
        decimal_places=2,
        required=True,
        initial=0,
    )  
    observations = forms.CharField(
        label="Descripción",
        max_length=40, 
        required=True,
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(3,'El nombre del Método de Pago es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ÑñÁÉÍÓÚáéíóú]*$','El nombre del Método de Pago esta mal formado','invalid_name')
        ]
    )
    observations.widget.attrs.update({
        'placeholder':'Opcional: Escriba una descripción'
    })
    date = forms.DateField(
        label="Fecha del movimiento",
        required=True,
        input_formats=['%Y/%m/%d']
    )
