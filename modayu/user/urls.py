from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet

app_name = 'user'

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]