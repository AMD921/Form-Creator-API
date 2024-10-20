from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_private']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")
        return value

    def validate_username(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            is_private=validated_data['is_private']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
