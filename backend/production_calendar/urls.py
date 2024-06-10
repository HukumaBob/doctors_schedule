from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CalendarDayViewSet


app_name = 'production_calendar'
router = DefaultRouter()
router.register(r'calendar_days', CalendarDayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
