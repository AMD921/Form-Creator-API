from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProcessSerializer
from .serializers import FormSerializer
from .serializers import QuestionSerializer, AnswerSerializer, CategorySerializer
from .models import Form
from report.models import Report
from .models import Process
from .models import Question, Answer, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    permission_classes = [ IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Amin
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save()

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        
        report, created = Report.objects.get_or_create(
            related_object_id=instance.id,
            report_type='form',
        )

        report.total_views += 1
        report.save()

        total_responses = Answer.objects.filter(question__form=instance).count()
        report.total_responses = total_responses
        report.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    