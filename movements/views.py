from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from movements.filters import MovementFilter
from django_tables2 import MultiTableMixin, LazyPaginator, Table
from django.views.generic.base import TemplateView
from django.db.models import Sum
from .tables import MovementTable, OriginTable, TypeTable, CategoryTable, PayMethodTable
from .tables import DJANGO_TABLES2_TABLE_ATTRS, TotalAmountMixin
from movements.models import (Movement, Type, Category, Pay_Method, Origin)
from movements.forms import (CategoryForm, MovementForm, PayMethodForm, TypeForm, OriginForm)


TEMPLATE_NAME = "mainapp/index.html"

# Multiple Tables in index.html
def balance_general(request):
    movements_total = Movement.objects.aggregate(total=Sum('amount'))['total'] or 0
    origins_total = Origin.objects.annotate(total_amount=Sum('movement__amount')).values('total_amount').first()['total_amount'] or 0
    types_total = Type.objects.annotate(total_amount=Sum('category__movement__amount')).values('total_amount').first()['total_amount'] or 0
    categories_total = Category.objects.annotate(total_amount=Sum('movement__amount')).values('total_amount').first()['total_amount'] or 0
    paymethods_total = Pay_Method.objects.annotate(total_amount=Sum('movement__amount')).values('total_amount').first()['total_amount'] or 0
    
    movements_table = MovementTable(Movement.objects.all())
    origins_table = OriginTable(Origin.objects.all())
    types_table = TypeTable(Type.objects.all())
    categories_table = CategoryTable(Category.objects.all())
    paymethods_table = PayMethodTable(Pay_Method.objects.all())
    
    return render(request, TEMPLATE_NAME, {
        'movements_total': movements_total,
        'origins_total': origins_total,
        'types_total': types_total,
        'categories_total': categories_total,
        'paymethods_total': paymethods_total,
        'movements_table': movements_table,
        'origins_table': origins_table,
        'types_table': types_table,
        'categories_table': categories_table,
        'paymethods_table': paymethods_table,
    })

# Using django_tables2
class AllMovementsTable(SingleTableMixin, FilterView):
    table_class = MovementTable
    model = Movement
    template_name = "movements/all_movements.html"
    filterset_class = MovementFilter


def origin_table_view(request):
    origins = Origin.objects.annotate(total_amount = Sum('movement__amount'))
    
    table = OriginTable(origins)
    return render(request, 'origins/origins.html', {'table': table})

# To create new parameters
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
            messages.success(request, 'Nuevo Tipo de movimiento, creado')

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

def create_pay_method(request):
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
        
        # To get the id of the user who is loged
        userid = request.user.id
        user_loged = User.objects.get(id=userid)
        
        # Take the form's data from the forms.py
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
            user= user_loged
            
            # Set the data that will be stored in the DB
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
            # Save the data into de the DB
            movement.save()
            messages.success(request, 'Nuevo movimiento creado')

            return redirect('create_movement')

    else:
        movementForm = MovementForm()

    return render(request, 'creates/create_movement.html', {
        'form':movementForm
    })

# Obtain a page for each element using slug in URL
def category(request, slug):
    category = Category.objects.get(slug=slug)

    return render(request, 'categories/category.html', {
        'category': category
    })

def type(request, slug):
    type = Type.objects.get(slug=slug)

    return render(request, 'types/types.html',{
        'type': type
    })

def pay_method(request, slug):
    payMethod = Pay_Method.objects.get(slug=slug)

    return render(request, 'pay_methods/pay_methods.html',{
        'payMethodSlug': payMethod
    })
