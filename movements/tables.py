import django_tables2 as tables
from .models import Movement

class MovementsTable(tables.Table):
    class Meta:
        model = Movement
        exclude = ("id", "idUser", "slug",)
        sequence = ("date",)
        DJANGO_TABLES2_TABLE_ATTRS = {
            'class': 'table table-hover',
            'thead': {
                'class': 'table-light',
            },
        }