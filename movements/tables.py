import django_tables2 as tables
from .models import Movement

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django_filters import FilterSet


class MovementsTable(tables.Table):
    # To show a footer with the sum of all values of amount
    amount = Movement.objects.all()
    total_amount = "{:,.2f} €".format(sum(amount.values_list('amount', flat=True)))

    amount = tables.Column(
        footer = f"Total: {total_amount}",
    )

    class Meta:
        model = Movement
        exclude = ("id", "idUser", "slug",)
        sequence = ("date",)
        attrs = {
            'class' : 'table table-striped table-hover',
            'th' : {
                '_ordering': {
                    'orderable' : 'sortable',
                    'ascending' : 'ascend',
                    'descending' : 'descend'
                }
            }
        }
        template_name = "django_tables2/bootstrap5-responsive.html"
        orderable = True
