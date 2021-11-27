from rest_framework.mixins   import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework          import permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from django.db               import transaction

from .models                 import User_Tire, Tire
from .permissions            import Custompermission
from users.models            import User
from .serializers            import User_TireSerializer

class User_TireViewset(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset           = User_Tire.objects.all()
    serializer_class   = User_TireSerializer
    permission_classes = [Custompermission]

    @transaction.atomic
    def create(self, request, *args, **kwargs):

        if len(request.data) > 5:
            return Response('can not request over 5 requests', status=status.HTTP_400_BAD_REQUEST)
        try:
            for data in request.data:
                data['user'] = User.objects.get(userid=data['user']).pk
                data['tire'] = Tire.objects.get(trimid=data['tire']).pk
                if not User_Tire.objects.filter(user=data['user'], tire=data['tire']).exists():
                    serializer = self.get_serializer(data=data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                else:
                    raise ValidationError
            return Response(data={'detail':'regist success'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response('user does not exist', status=status.HTTP_400_BAD_REQUEST)
        except Tire.DoesNotExist:
            return Response('tire does not exist', status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        userid = self.request.query_params.get('id', None)
        try:
            user_pk    = User.objects.get(userid=userid).pk
            queryset   = self.get_queryset().filter(user=user_pk)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response('User Dose Not Exist',status=status.HTTP_404_NOT_FOUND)