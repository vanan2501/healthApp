from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics, parsers
from health.models import HealthProfile, User, ExercisePlan, DietPlan, Reminder, HealthLog
from health.serializers import HealthProfileSerializer, UserSerializer, ExercisePlanSerializer, DietPlanSerializer, ReminderSerializer, HealthLogSerializer


def index(request):
    return HttpResponse('')

class HealthProfileViewSet(viewsets.ModelViewSet):
    queryset = HealthProfile.objects.filter(active = True)
    serializer_class = HealthProfileSerializer


class UserViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser]

class ExercisePlanViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ExercisePlan.objects.filter(active = True)
    serializer_class = ExercisePlanSerializer

class DietPlanViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = DietPlan.objects.filter(active = True)
    serializer_class = DietPlanSerializer

class ReminderViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Reminder.objects.filter(active = True)
    serializer_class = ReminderSerializer

class HealthLogViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = HealthLog.objects.filter(active = True)
    serializer_class = HealthLogSerializer