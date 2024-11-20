from rest_framework import viewsets, mixins, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, TodoSerializer
from .models import Todo


class UserViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return super().perform_create(serializer)