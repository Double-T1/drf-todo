from rest_framework import viewsets, mixins, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, TodoSerializer
from .models import Todo
from .permissions import IsOwner, IsUser


class UserViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAdminUser]

        elif self.action == "create":
            permission_classes = [permissions.AllowAny]

        elif self.action == "retrieve" or (self.action == "destroy"):
            permission_classes = [
                permissions.IsAuthenticated,
                IsUser | permissions.IsAdminUser
            ]

        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)