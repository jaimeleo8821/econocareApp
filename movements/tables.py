import django_tables2 as tables
from .models import Movement
from math import fsum

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django_filters import FilterSet


class MovementsTable(tables.Table):
    
    amount = Movement.objects.all()
    total_amount = fsum(amount.values_list('amount', flat=True))

    amount = tables.Column(
        footer=f"Total: {total_amount}"
    )

    class Meta:
        model = Movement
        exclude = ("id", "idUser", "slug",)
        sequence = ("date",)
        DJANGO_TABLES2_TABLE_ATTRS = {
            'class': 'table table-dark table-hover',
        }
        template_name = "django_tables2/bootstrap5-responsive.html"
        orderable = True
