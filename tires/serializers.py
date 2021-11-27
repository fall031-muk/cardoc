from django.db.models  import fields
from rest_framework    import serializers

from .models           import Tire, User_Tire
from users.models      import User
from users.serializers import UserSerializer


class TireSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Tire
        fields = ['trimid', 'front_width', 'front_aspect_ratio', 'front_wheel_size', 'rear_width', 'rear_aspect_ratio', 'rear_wheel_size']


class User_TireSerializer(serializers.ModelSerializer):
    user = UserSerializer
    tire = TireSerializer

    class Meta:
        model  = User_Tire
        fields = ['user', 'tire']

    def create(self, validated_data):
        instance = User_Tire.objects.create(**validated_data)
        return instance

    def to_representation(self, instance):
        return {
            'user_id'                 : instance.user.userid,
            'trim_id'                 : instance.tire.trimid,
            'front_tire_width'        : instance.tire.front_width,
            'front_tire_aspect_ratio' : instance.tire.front_aspect_ratio,
            'front_tire_wheel_size'   : instance.tire.front_wheel_size,
            'rear_tire_width'         : instance.tire.rear_width,
            'rear_tire_aspect_ratio'  : instance.tire.rear_aspect_ratio,
            'rear_tire_wheel_size'    : instance.tire.rear_wheel_size
        }