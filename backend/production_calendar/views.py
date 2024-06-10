from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import CalendarDay
from .serializers import CalendarDaySerializer
from .filters import CalendarDayFilter

class CalendarDayViewSet(viewsets.ModelViewSet):
    queryset = CalendarDay.objects.all()
    serializer_class = CalendarDaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CalendarDayFilter
