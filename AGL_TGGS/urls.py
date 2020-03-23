from .views import index, division
from django.urls import path

urlpatterns = [
    path('', index, name='projects'),
    path('<int:project_gid>/', division, name='division'),
]