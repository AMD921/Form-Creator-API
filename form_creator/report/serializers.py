from rest_framework import serializers
from report.models import Report
from report.models import FormResponse
from report.models import ProcessResponse
from report.models import ReportLog
from report.models import PeriodicReport


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'id',
            'report_type',
            'related_object_id',
            'created_at',
            'updated_at',
            'total_views',
            'total_responses',
            ]
        read_only_fields = [
            'created_at',
            'updated_at',
            ]



class FormResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponse
        fields = [
            'id',
            'form',
            'user',
            'response_data',
            'submitted_at',
            ]
        read_only_fields = ['submitted_at']



class ProcessResponseSerializer(serializers.ModelSerializer):
    completed_forms = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=FormResponse.objects.all(),
        )

    class Meta:
        model = ProcessResponse
        fields = [
            'id',
            'process',
            'user',
            'completed_forms',
            'started_at',
            'completed_at',
            ]
        read_only_fields = ['started_at']


class ReportLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportLog
        fields = [
            'id',
            'report',
            'change_type',
            'change_data',
            'timestamp',
            ]
        read_only_fields = ['timestamp']



class PeriodicReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicReport
        fields = [
            'id',
            'report',
            'frequency',
            'last_sent_at',
            ]
        read_only_fields = ['last_sent_at']
