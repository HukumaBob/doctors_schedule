from django.contrib import admin

from .models import (
    User,
    UserProfile,
    UserProfileModality,
    Specialization
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in User._meta.fields
        ]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in UserProfile._meta.fields
        ]
    
@admin.register(UserProfileModality)
class UserProfileModalityAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in UserProfileModality._meta.fields
        ]    

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Specialization._meta.fields
        ]

