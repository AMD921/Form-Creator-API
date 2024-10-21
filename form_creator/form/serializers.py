from rest_framework import serializers
from .models import Form
from .models import Process

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'is_public', 'created_at', 'updated_at', 'question']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'title', 'description', 'is_public', 'created_by', 'updated_at', 'form', 'password', 'type', 'user']