"""
URL configuration for healthApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from health import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="vanan25012002@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,

)


r = routers.DefaultRouter()
r.register('HealthProfiles', views.HealthProfileViewSet)
r.register('Users', views.UserViewSet)
r.register('ExercisePlans', views.ExercisePlanViewSet)
r.register('DietPlans', views.DietPlanViewSet)
r.register('Reminders', views.ReminderViewSet)
r.register('HealthLog', views.HealthLogViewSet)

urlpatterns = [
    path('o/',include('oauth2_provider.urls')),
    path('admin/', admin.site.urls),
    path('', include(r.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
