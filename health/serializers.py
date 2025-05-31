from rest_framework import serializers
from health.models import HealthProfile, User, ExercisePlan, DietPlan, Reminder, HealthLog

class HealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        u = User(**validated_data)
        u.set_password(u.password)
        u.save()
        return u
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password','avatar']
        extra_kwargs = {
            'password':{
                "write_only": True
            }
        }

class ExercisePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercisePlan
        fields = '__all__'


class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class HealthLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthLog
        fields = '__all__'