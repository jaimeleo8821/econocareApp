from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from movements.models import Movement, Type, Category, Pay_Method
from movements.forms import FormCategory, FormMovement, FormPayMethod, FormType

# Create your views here.
def create_type(request):
    if request.method == 'POST':

        typeForm = FormType(request.POST)

        if typeForm.is_valid():
            data_form = typeForm.cleaned_data

            type = data_form.get('movement_type')
            
            type = Type(
                type = type
            )
            type.save()

            return redirect('create_type')

    else:
        typeForm = FormType()

    return render(request, 'types/create_type.html', {
        'form':typeForm
    })

def create_category(request):
    if request.method == 'POST':

        categoryForm = FormCategory(request.POST)

        if categoryForm.is_valid():
            data_form = categoryForm.cleaned_data
            types = data_form['id']
            category = data_form.get('category')
            
            category = Category(
                idType = types,  # Aquí debe ir la ForeignKey de Type 'idType_id'
                category = category
            )

            category.save()

            return redirect('create_category')

    else:
        categoryForm = FormCategory()

    return render(request, 'types/create_category.html', {
        'form':categoryForm
    })

def create_payMethod(request):
    if request.method == 'POST':

        payMethodForm = FormPayMethod(request.POST)

        if payMethodForm.is_valid():
            data_form = payMethodForm.cleaned_data

            pay_method = data_form.get('pay_method')
            
            method = Pay_Method(
                payMethod = pay_method
            )
            method.save()

            return redirect('create_pay_method')

    else:
        payMethodForm = FormPayMethod()

    return render(request, 'types/create_pay_method.html', {
        'form':payMethodForm
    })

def create_movement(request):
    if request.method == 'POST':

        movementForm = FormMovement(request.POST)

        if movementForm.is_valid():
            data_form = movementForm.cleaned_data
            date = data_form.get('date')
            amount = data_form.get('amount')
            type = data_form['idType']
            category = data_form['idCategory']
            paymethod = data_form['idPayMethod']
            observations = data_form.get('observations')
            user = data_form['user']
            
            category = Category(
                date = date,
                amount = amount,
                idType = type,  # Aquí debe ir la ForeignKey de Type 'idType_id'
                idCategory = category,
                idPayMethod = paymethod,
                observations = observations,
                user = user
            )

            category.save()

            return redirect('create_movement')

    else:
        movementForm = FormMovement()

    return render(request, 'types/create_movement.html', {
        'form':movementForm
    })


