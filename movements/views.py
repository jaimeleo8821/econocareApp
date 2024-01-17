from django.http import HttpResponse
from django.shortcuts import render, redirect
from movements.models import Movement, Type, Category, Pay_Method
from movements.forms import FormCategory, FormPayMethod, FormType

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

            type = data_form.get('type')
            category = data_form.get('category')
            
            category = Category(
                #type = type,  # Aquí debe ir la ForeignKey de Type 'idType_id'
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



