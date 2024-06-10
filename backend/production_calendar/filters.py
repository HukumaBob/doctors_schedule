from django_filters import rest_framework as filters
from .models import CalendarDay

class CalendarDayFilter(filters.FilterSet):
    year = filters.NumberFilter(field_name="date", lookup_expr='year')
    month = filters.NumberFilter(field_name="date", lookup_expr='month')
    day = filters.NumberFilter(field_name="date", lookup_expr='day')
    week = filters.NumberFilter(field_name="date", lookup_expr='week')

    class Meta:
        model = CalendarDay
        fields = ['year', 'month', 'day', 'week']
