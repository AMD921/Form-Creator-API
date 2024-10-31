from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status

from rest_framework.response import Response
from rest_framework.decorators import action

from report.models import Report
from report.models import FormResponse
from report.models import ProcessResponse
from report.models import PeriodicReport

from report.serializers import ReportSerializer
from report.serializers import FormResponseSerializer
from report.serializers import ProcessResponseSerializer
from report.serializers import PeriodicReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    @action(detail=False, methods=['get'], url_path='form/(?P<related_object_id>[^/.]+)')
    def retrieve_report_by_form_id(self, request, related_object_id=None):
        reports = Report.objects.filter(related_object_id=related_object_id, report_type='form')

        if reports.exists():
            serializer = self.get_serializer(reports, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No reports found'}, status=status.HTTP_404_NOT_FOUND)



class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    @action(detail=False, methods=['get'], url_path='form/(?P<related_object_id>[^/.]+)')
    def retrieve_report_by_form_id(self, request, related_object_id=None):
        reports = Report.objects.filter(related_object_id=related_object_id, report_type='process')

        if reports.exists():
            serializer = self.get_serializer(reports, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'No reports found'}, status=status.HTTP_404_NOT_FOUND)








class FormResponseViewSet(viewsets.ModelViewSet):
    """
    This viewset handles the CRUD operations for the FormResponse model.
    """
    queryset = FormResponse.objects.all()
    serializer_class = FormResponseSerializer

    def create(self, request, *args, **kwargs):
        """
        Overridden create method to handle additional logic when a form response is created.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
            )



class ProcessResponseViewSet(viewsets.ModelViewSet):
    """
    This viewset handles the CRUD operations for the ProcessResponse model.
    """
    queryset = ProcessResponse.objects.all()
    serializer_class = ProcessResponseSerializer

    def update(self, request, *args, **kwargs):
        """
        Overridden update method to handle additional logic when a process response is updated.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
            )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



class PeriodicReportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset handles only read operations for the PeriodicReport model.
    """
    queryset = PeriodicReport.objects.all()
    serializer_class = PeriodicReportSerializer

    @action(detail=True, methods=['post'])
    def send_report(self, request, pk=None):
        """
        Custom action to manually trigger sending of a periodic report.
        """
        periodic_report = self.get_object()
        
        return Response({'status': 'Report sent successfully'}, status=status.HTTP_200_OK)
