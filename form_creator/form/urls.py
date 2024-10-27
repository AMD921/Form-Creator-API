from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import QuestionViewSet, AnswerViewSet, CategoryViewSet, ProcessViewSet, FormViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'processes', ProcessViewSet)
router.register(r'forms', FormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
