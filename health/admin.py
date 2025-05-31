from django.contrib import admin

from.models import HealthProfile
from.models import DietPlan, User, ExercisePlan
# Register your models here.

admin.site.register(HealthProfile)
admin.site.register(DietPlan)
admin.site.register(User)
admin.site.register(ExercisePlan)