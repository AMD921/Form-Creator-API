from django.test import TestCase
from .models import User
from .serializers import UserSerializer

class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'TestPassword123',
            'is_private': False
        }
        self.serializer = UserSerializer(data=self.user_data)

    def test_valid_user_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_invalid_email(self):
        self.user_data['email'] = 'invalid-email'
        serializer = UserSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_invalid_username_too_short(self):
        self.user_data['username'] = 'tu'
        serializer = UserSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_non_unique_username(self):
        User.objects.create(**self.user_data)
        serializer = UserSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)

    def test_invalid_password(self):
        self.user_data['password'] = 'short'
        serializer = UserSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
