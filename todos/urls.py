from . import views
from django.urls import path, include
from rest_framework import routers

app_name = "todos"

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")
router.register(r"todo", views.TodoViewSet, basename="todo")

urlpatterns = [
    path("", include(router.urls))
]


