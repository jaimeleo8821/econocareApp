from movements.models import (Movement, Type, Category, Pay_Method, Origin)
import django_tables2 as tables
from django.db.models import Sum
from django_tables2 import LazyPaginator

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap5-responsive.html"

DJANGO_TABLES2_TABLE_ATTRS = {
    'class': 'table table-hover',
    'thead': {
        'class': 'table-light',
    },
}
ACCESSOR = "total_amount"
VERBOSE_NAME = "Total Amount"

class TotalAmountMixin:
    total_amount = tables.Column(accessor=ACCESSOR, verbose_name=VERBOSE_NAME)

    def render_total_amount(self, value, record):
        return value

class BaseTable(TotalAmountMixin, tables.Table):
    class Meta:
        template_name = DJANGO_TABLES2_TEMPLATE
        attrs = DJANGO_TABLES2_TABLE_ATTRS
        exclude = ("id", "slug")

class MovementTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Movement
        sequence = ("date", "idOrigin", "idType", "idCategory", "idPayMethod", "amount", "observations")
        order_by = ("-date",)
        paginator_class = LazyPaginator
        localize = ("amount",)

class OriginTable(BaseTable):
    origin = tables.Column()

    class Meta(BaseTable.Meta):
        model = Origin

class TypeTable(BaseTable):
    type = tables.Column()

    class Meta(BaseTable.Meta):
        model = Type

class CategoryTable(BaseTable):
    category = tables.Column()

    class Meta(BaseTable.Meta):
        model = Category

class PayMethodTable(BaseTable):
    paymethod = tables.Column()

    class Meta(BaseTable.Meta):
        model = Pay_Method