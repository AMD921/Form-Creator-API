from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from report.views import ReportViewSet
from report.views import ProcessViewSet
# from report.viewsets import FormResponseViewSet
# from report.viewsets import ProcessResponseViewSet


router = DefaultRouter()
router.register(r'reports', ReportViewSet, basename='reports')
router.register(r'process_reports', ProcessViewSet, basename='process_reports')
# router.register(r'form-responses', FormResponseViewSet, basename='form-reports')
# router.register(r'process-responses', ProcessResponseViewSet, basename='process-reports')

urlpatterns = [
    path('', include(router.urls)),
    path('forms/<int:related_object_id>/', ReportViewSet.as_view({'get': 'retrieve_report_by_form_id'})),
    path('process/<int:related_object_id>/', ProcessViewSet.as_view({'get': 'retrieve_report_by_form_id'})),
]
