from django.http import HttpResponse
from django.shortcuts import render, redirect
from movements.models import Movement, Type, Category, Pay_Method, Origin
from movements.forms import CategoryForm, MovementForm, PayMethodForm, TypeForm, OriginForm
from django.contrib import messages

# Create your views here.
def create_type(request):
    if request.method == 'POST':

        typeForm = TypeForm(request.POST)

        if typeForm.is_valid():
            data_form = typeForm.cleaned_data

            type = data_form.get('movement_type')
            
            type = Type(
                type = type
            )
            type.save()

            return redirect('create_type')

    else:
        typeForm = TypeForm()

    return render(request, 'creates/create_type.html', {
        'form':typeForm
    })

def create_origin(request):
    if request.method == 'POST':

        originForm = OriginForm(request.POST)

        if originForm.is_valid():
            data_form = originForm.cleaned_data
            origin = data_form.get('origin')
            origin = Origin(
                origin = origin
            )
            origin.save()

            return redirect('create_origin')

    else:
        originForm = OriginForm()

    return render(request, 'creates/create_origin.html', {
        'form':originForm
    })

def create_category(request):
    if request.method == 'POST':

        categoryForm = CategoryForm(request.POST)

        if categoryForm.is_valid():
            data_form = categoryForm.cleaned_data
            types = data_form.get('type')
            category = data_form.get('category')
            
            category = Category(
                idType = types,
                category = category
            )

            category.save()

            # Mensaje Flash
            messages.success(request, f'Haz creado correctamente la Categoría {category.category}')

            return redirect('create_category')

    else:
        categoryForm = CategoryForm()

    return render(request, 'creates/create_category.html', {
        'form':categoryForm
    })

def create_payMethod(request):
    if request.method == 'POST':

        payMethodForm = PayMethodForm(request.POST)

        if payMethodForm.is_valid():
            data_form = payMethodForm.cleaned_data

            pay_method = data_form.get('pay_method')
            
            method = Pay_Method(
                payMethod = pay_method
            )
            method.save()

            return redirect('create_pay_method')

    else:
        payMethodForm = PayMethodForm()

    return render(request, 'creates/create_pay_method.html', {
        'form':payMethodForm
    })

def create_movement(request):
    if request.method == 'POST':

        movementForm = MovementForm(request.POST)

        if movementForm.is_valid():
            
            data_form = movementForm.cleaned_data
            origin = data_form.get('idOrigin')
            types = data_form.get('idType')
            category = data_form.get('idCategory')
            paymethod = data_form.get('idPayMethod')
            amount = data_form.get('amount')
            date = data_form.get('date')
            observations = data_form.get('observations')         
            user = data_form.get('idUser')
            
            movement = Movement(
                idOrigin = origin,
                idType = types,
                idCategory = category,
                idPayMethod = paymethod,
                amount = amount,
                observations = observations,
                date = date,
                idUser = user 
            )

            movement.save()

            return redirect('create_movement')

    else:
        movementForm = MovementForm()

    return render(request, 'creates/create_movement.html', {
        'form':movementForm
    })

def category(request, slug):

    category = Category.objects.order_by('category').get(slug=slug)

    return render(request, 'categories/categories.html', {
        'category': category
    })
