from rest_framework.mixins   import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework          import permissions
from .models                 import User
from .serializers            import UserSerializer

class UserViewset(CreateModelMixin, GenericViewSet):
    queryset         = User.objects.all()
    serializer_class = UserSerializer