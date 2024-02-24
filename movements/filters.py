from decimal import Decimal
from django.db.models import Q
import django_filters
from movements.models import Movement

class MovementFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Movement
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Movement.objects.filter(
                Q(amount=value) | Q(date=value)
            )

        return Movement.objects.filter(
            Q(idOrigin__icontains=value) | Q(idType__icontains=value) | Q(idCategory__icontains=value) | Q(idPayMethod__icontains=value)
        )