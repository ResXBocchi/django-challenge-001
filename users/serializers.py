from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

class UserDetailsSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='uuid')
    name = serializers.CharField(source='username')
    class Meta:
        model = User
        fields = ('id','name','picture')