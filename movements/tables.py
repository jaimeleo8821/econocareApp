from movements.models import (Movement, Type, Category, Pay_Method, Origin)
import django_tables2 as tables

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap5-responsive.html"

DJANGO_TABLES2_TABLE_ATTRS = {
    'class': 'table table-hover',
    'thead': {
        'class': 'table-light',
    },
}

class MovementTable (tables.Table):
    class Meta:
        model = Movement
        template_name = DJANGO_TABLES2_TEMPLATE
        sequence = ("date", "idOrigin", "idType", "idCategory", "idPayMethod", "amount", "observations")
        exclude = ("id", "idUser", "slug")
        order_by = ("-date",)
        paginator_class = tables.LazyPaginator
        attrs = DJANGO_TABLES2_TABLE_ATTRS
        localize = ("amount",)


class OriginTable(tables.Table):
    origin = tables.Column()
    total_amount = tables.Column(accessor='total_amount', verbose_name='Total Amount')

    def render_total_amount(self, value, record):
        return value

    class Meta:
        model = Origin
        template_name = DJANGO_TABLES2_TEMPLATE
        attrs = DJANGO_TABLES2_TABLE_ATTRS
        exclude = ("id", "slug")


class TypeTable(tables.Table):
    type = tables.Column()
    total_amount = tables.Column(accessor='total_amount', verbose_name='Total Amount')

    def render_total_amount(self, value, record):
        return value

    class Meta:
        model = Type
        template_name = DJANGO_TABLES2_TEMPLATE
        attrs = DJANGO_TABLES2_TABLE_ATTRS
        exclude = ("id", "slug")

class CategoryTable(tables.Table):
    category = tables.Column()
    total_amount = tables.Column(accessor='total_amount', verbose_name='Total Amount')

    def render_total_amount(self, value, record):
        return value

    class Meta:
        model = Category
        template_name = DJANGO_TABLES2_TEMPLATE
        attrs = DJANGO_TABLES2_TABLE_ATTRS
        exclude = ("id", "slug")


class PayMethodTable(tables.Table):
    paymethod = tables.Column()
    total_amount = tables.Column(accessor='total_amount', verbose_name='Total Amount')

    def render_total_amount(self, value, record):
        return value

    class Meta:
        model = Pay_Method
        template_name = DJANGO_TABLES2_TEMPLATE
        attrs = DJANGO_TABLES2_TABLE_ATTRS
        exclude = ("id", "slug")