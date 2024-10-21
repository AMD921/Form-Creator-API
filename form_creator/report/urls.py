from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from report.viewsets import ReportViewSet
from report.viewsets import FormResponseViewSet
from report.viewsets import ProcessResponseViewSet


router = DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'form-responses', FormResponseViewSet)
router.register(r'process-responses', ProcessResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
