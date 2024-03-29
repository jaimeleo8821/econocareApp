from unicodedata import category
from movements.models import Type, Category, Pay_Method, Movement, Origin

def get_categories(request):
    categories = Category.objects.order_by('category').values_list('id', 'category', 'slug', 'idType' )

    return {
        'categories': categories
    }

def get_types(request):
    types = Type.objects.order_by('type').values_list('id', 'type', 'slug')

    return {
        'types': types
    }

def get_origins(request):
    origins = Origin.objects.order_by('origin').values_list('id', 'origin', 'slug')

    return {
        'origins': origins
    }

def get_pay_methods(request):
    payMethods = Pay_Method.objects.order_by('payMethod').values_list('id', 'payMethod', 'slug')

    return {
        'pay_methods': payMethods
    }

def get_movements(request):
    movements = Movement.objects.values_list('id', 'idOrigin', 'idType', 'idCategory', 'idPayMethod', 'amount', 'observations', 'date', 'idUser', 'slug')

    return {
        'movements': movements
    }