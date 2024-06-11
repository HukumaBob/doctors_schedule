from django_filters import rest_framework as filters

from .models import Modality
from .models import UserProfile

class UserProfileFilter(filters.FilterSet):
    position = filters.CharFilter(field_name='position')
    modality = filters.ModelMultipleChoiceFilter(
        field_name='modality__id', 
        to_field_name='id',
        queryset=Modality.objects.all()
    )
    priority = filters.BooleanFilter(field_name='modality__priority')

    class Meta:
        model = UserProfile
        fields = ['position', 'modality', 'priority']
