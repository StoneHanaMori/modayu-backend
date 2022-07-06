
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='user_info:user-detail',
        lookup_field='username'
    )

    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'last_login',
            'date_joined',
        ]