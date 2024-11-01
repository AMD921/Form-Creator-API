from rest_framework import serializers
from .models import Form
from .models import Process
from .models import Question, Answer, Category

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['title', 'description', 'is_public', 'created_at', 'updated_at', 'question']
        read_only_fields = ['created_at', 'updated_at', 'user']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'title', 'description', 'is_public', 'created_at', 'updated_at', 'form', 'password', 'type', 'user']
        read_only_fields =  ['created_at', 'updated_at']
#Amin
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'question_text',
            'type',
            'created_at',
            'updated_at',
            #'answer',
            ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
            'question',
            'text',
            ]

# Serializer for Category Model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'user',
            'name',
            'question',
            'process',
            ]