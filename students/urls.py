from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)  # Endpoint: /students/

urlpatterns = [
    path('', include(router.urls)),
]