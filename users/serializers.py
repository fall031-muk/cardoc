from rest_framework            import serializers
from .models                   import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model   = User
        fields  = ['id', 'userid', 'password', 'is_staff']

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance