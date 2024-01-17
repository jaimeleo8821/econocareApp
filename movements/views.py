from django.http import HttpResponse
from django.shortcuts import render, redirect
from movements.models import Movement, Type, Category, Pay_Method
from movements.forms import FormType

# Create your views here.
def save_type(request):
    type = Type(
        type = type
    )
    type.save()

    return HttpResponse(f"Tipo de movimiento creado: <strong>{type.type}</strong> ")

def create_type(request):
    if request.method == 'POST':

        typeForm = FormType(request.POST)

        if typeForm.is_valid():
            data_form = typeForm.cleaned_data

            type = data_form.get('type')
            
            type = Type(
                type = type
            )
            type.save()

            return redirect('create')

    else:
        typeForm = FormType()

    return render(request, 'types/create_type.html', {
        'form':typeForm
    })


