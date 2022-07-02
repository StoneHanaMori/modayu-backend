from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('generate', views.generate, name='generate')
]