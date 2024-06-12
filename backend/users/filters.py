from django_filters import rest_framework as filters

from .models import UserProfile

class ModalityPriorityFilter(filters.Filter):
    def filter(self, qs, value):
        if value in (None, ''):
            return qs
        modality, priority = value.split(',')
        priority = priority.lower() in ['true', '1']
        return qs.filter(userprofilemodality__modality__modality=modality, userprofilemodality__priority=priority)

class UserProfileFilter(filters.FilterSet):
    position = filters.CharFilter(field_name='position')
    modality_priority = ModalityPriorityFilter()
    first_name = filters.CharFilter(field_name='user__first_name', lookup_expr='icontains')
    last_name = filters.CharFilter(field_name='user__last_name', lookup_expr='icontains')

    class Meta:
        model = UserProfile
        fields = ['position', 'modality_priority', 'first_name', 'last_name']
