from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('estado', views.health_check, name='health_check'),
    path("projects/", views.project_list, name="project_list"),
    path("tasks/", views.task_list, name="task_list"),

]

router = DefaultRouter()
router.register(r"projects", views.ProjectViewSet)
router.register(r"tasks", views.TaskViewSet, basename="task")
urlpatterns += router.urls 