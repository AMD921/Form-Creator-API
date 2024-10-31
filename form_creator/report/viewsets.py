# from rest_framework import viewsets
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import action

# from report.models import Report
# from report.models import FormResponse
# from report.models import ProcessResponse
# from report.models import ReportLog
# from report.models import PeriodicReport

# from report.serializers import ReportSerializer
# from report.serializers import FormResponseSerializer
# from report.serializers import ProcessResponseSerializer
# from report.serializers import ReportLogSerializer
# from report.serializers import PeriodicReportSerializer







        

# class FormResponseViewSet(viewsets.ModelViewSet):
#     queryset = FormResponse.objects.all()
#     serializer_class = FormResponseSerializer

    
#     @action(detail=False, methods=['get'])
#     def filter_by_form(self, request):
#         form_id = request.query_params.get('form_id')
#         if form_id:
#             responses = self.queryset.filter(form_id=form_id)
#             serializer = self.get_serializer(responses, many=True)
#             return Response(serializer.data)
#         return Response({'error': 'Form ID not provided'}, status=400)



# class ProcessResponseViewSet(viewsets.ModelViewSet):
#     queryset = ProcessResponse.objects.all()
#     serializer_class = ProcessResponseSerializer

    
#     @action(detail=True, methods=['post'])
#     def mark_completed(self, request, pk=None):
#         process_response = self.get_object()
#         process_response.completed_at = timezone.now()
#         process_response.save()
#         return Response({'status': 'process marked as completed', 'completed_at': process_response.completed_at})



# class ReportLogViewSet(viewsets.ModelViewSet):
#     queryset = ReportLog.objects.all()
#     serializer_class = ReportLogSerializer



# class PeriodicReportViewSet(viewsets.ModelViewSet):
#     queryset = PeriodicReport.objects.all()
#     serializer_class = PeriodicReportSerializer

    
#     @action(detail=True, methods=['post'])
#     def send_report(self, request, pk=None):
#         periodic_report = self.get_object()
        
#         return Response({'status': 'report sent', 'report': str(periodic_report)})
