from django.urls import path, include
from article import views
from article.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

app_name = 'article'
router = DefaultRouter()
router.register(r'', ArticleViewSet)
urlpatterns = [
    path('generate', views.generate, name='generate'),
    # path('', include(router.urls))
]