from django.urls import path
from . import views

app_name = 'functional_points'

urlpatterns = [
    path('', views.functional_points, name='functional_points'),
]