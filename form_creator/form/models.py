from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class Form(models.Model):
    title = models.CharField( max_length=255)
    description = models.TextField(null= True, blank= True)
    is_public = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    question = models.ForeignKey('question', on_delete=models.CASCADE)

class PROCESS_TYPE_CHOICES(Enum):
    linear = 'l'
    free = 'f'
        
    @classmethod
    def choices(cls):
        return [
            (cls.linear.value, 'Linear'),
            (cls.free.value, 'Free'),
        ]
    

class Process(models.Model):
    title = models.CharField( max_length=255)
    description = models.TextField(null= True)
    is_public = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    form = models.ForeignKey(Form, on_delete= models.CASCADE)
    password = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=10, choices= PROCESS_TYPE_CHOICES.choices())
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    
# Create your models here.
