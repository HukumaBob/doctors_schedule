from rest_framework import serializers

from medical_examination.models import Modality
from .models import Specialization, User, UserProfile, UserProfileModality


class UserProfileModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModality
        fields = ['modality', 'priority']

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    modality = UserProfileModalitySerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'middle_name', 'phone', 'place_of_work', 'position', 'specialization', 'modality', 'wage_rate', 'operating_mode']

    def create(self, validated_data):
        modality_data = validated_data.pop('modality')
        user_profile = UserProfile.objects.create(**validated_data)
        for modality_data_item in modality_data:
            UserProfileModality.objects.create(user_profile=user_profile, **modality_data_item)
        return user_profile

    def update(self, instance, validated_data):
        modality_data = validated_data.pop('modality')
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.place_of_work = validated_data.get('place_of_work', instance.place_of_work)
        instance.position = validated_data.get('position', instance.position)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.wage_rate = validated_data.get('wage_rate', instance.wage_rate)
        instance.operating_mode = validated_data.get('operating_mode', instance.operating_mode)
        instance.save()

        for modality_item in modality_data:
            modality_id = modality_item.get('id', None)
            if modality_id:
                modality_instance = UserProfileModality.objects.get(id=modality_id, user_profile=instance)
                modality_instance.modality = modality_item.get('modality', modality_instance.modality)
                modality_instance.priority = modality_item.get('priority', modality_instance.priority)
                modality_instance.save()
            else:
                UserProfileModality.objects.create(user_profile=instance, **modality_item)
        return instance