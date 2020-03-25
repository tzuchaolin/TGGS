from .views import index, project
from django.urls import path

urlpatterns = [
    path('projects/', index, name='projects'),
    path('projects/<int:project_gid>/', project, name='division'),
]