from rest_framework import serializers
from .models import CalendarDay, ExaminationSchedule

class ExaminationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExaminationSchedule
        fields = ['examination', 'predicted_count', 'actual_count']

class CalendarDaySerializer(serializers.ModelSerializer):
    examination_schedule = serializers.SerializerMethodField()

    class Meta:
        model = CalendarDay
        fields = ['date', 'day_type', 'work_hours', 'examination_schedule']

    def get_examination_schedule(self, obj):
        schedule = ExaminationSchedule.objects.filter(day=obj)
        serializer = ExaminationScheduleSerializer(schedule, many=True)
        return serializer.data
