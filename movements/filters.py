from django_filters import FilterSet
from movements.models import (Movement, Type, Category, Pay_Method, Origin)

class MovementFilter(FilterSet):
    class Meta:
        model = Movement
        fields = {"date":["exact",], "idOrigin":["exact",]}