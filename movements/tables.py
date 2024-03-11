from .models import Movement
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
