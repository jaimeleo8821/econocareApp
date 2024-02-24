from .models import Movement
import django_tables2 as tables

class MovementHTMxTable (tables.Table):
    class Meta:
        model = Movement
        template_name = "tables/bootstrap_htmx.html"

