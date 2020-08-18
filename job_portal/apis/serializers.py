from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.conf import settings

from .models import Posts, CustomUser as MyUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'user', 'user_type')
        extra_kwargs = { 'password': { 'write_only': True } }

    def create(self, validated_data):
        user = MyUser(
            email = validated_data['email'],
            user = validated_data['user'],
            user_type = validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user