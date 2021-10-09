from django.urls import path
from . import views

app_name = 'cocomo2'

urlpatterns = [
    path('', views.cocomo2_start, name='cocomo2_start'),
    path('preliminary_assessment/', views.preliminary_assessment, name="preliminary_assessment"),
    path('detailed_assessment/', views.detailed_assessment, name="detailed_assessment"),
]