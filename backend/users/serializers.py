from rest_framework import serializers

from medical_examination.models import Modality

from .models import Specialization, User, UserProfile, UserProfileModality

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['specialization']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserProfileModalitySerializer(serializers.ModelSerializer):
    modality = serializers.PrimaryKeyRelatedField(queryset=Modality.objects.all())
    class Meta:
        model = UserProfileModality
        fields = ['modality', 'priority']

class UserProfileSerializer(serializers.ModelSerializer):
    userprofilemodality_set = UserProfileModalitySerializer(many=True)
    specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all())
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = [
            'user', 
            'middle_name',
            'phone', 
            'place_of_work', 
            'position', 
            'specialization', 
            'userprofilemodality_set', 
            'wage_rate', 
            'operating_mode'
            ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        specialization = validated_data.pop('specialization')
        userprofilemodality_set_data = validated_data.pop('userprofilemodality_set')

        # Create and save User object
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Create UserProfile object with the saved specialization
        user_profile = UserProfile.objects.create(user=user, specialization=specialization, **validated_data)

        # Create or update UserProfileModality objects using the saved user_profile
        for upm_data in userprofilemodality_set_data:
            print(upm_data)
            modality, created = UserProfileModality.objects.update_or_create(
                user_profile=user_profile, 
                modality=upm_data['modality'], 
                defaults={'priority': upm_data['priority']}
            )

        return user_profile

    def update(self, instance, validated_data):
        # Обновление данных пользователя
        user_data = validated_data.pop('user', None)
        if user_data is not None:
            user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        # Обновление специализации
        specialization = validated_data.pop('specialization', None)
        if specialization is not None:
            instance.specialization = specialization

        # Обновление UserProfileModality
        userprofilemodality_set_data = validated_data.pop('userprofilemodality_set', [])
        for upm_data in userprofilemodality_set_data:
            modality, created = UserProfileModality.objects.update_or_create(
                user_profile=instance, 
                modality=upm_data['modality'], 
                defaults={'priority': upm_data['priority']}
            )

        # Обновление остальных полей
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

