from django.db import models
from form.models import Form
from form.models import Process
from user.models import User



class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('form', 'Form'),
        ('process', 'Process')
    ]
    report_type = models.CharField(
        max_length=10,
        choices=REPORT_TYPE_CHOICES
        )
    related_object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    total_responses = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [
            'report_type',
            'related_object_id',
            ]

    def __str__(self):
        return f"{self.get_report_type_display()} - {self.related_object_id}"


class FormResponse(models.Model):
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='responses',
        )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        )
    response_data = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.form} by {self.user or 'Anonymous'}"


class ProcessResponse(models.Model):
    process = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
        related_name='responses',
        )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        )
    completed_forms = models.ManyToManyField(
        FormResponse,
        related_name='completed_in_process',
        )
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        )

    def __str__(self):
        return f"Response to {self.process} by {self.user or 'Anonymous'}"


class ReportLog(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name='logs',
        )
    change_type = models.CharField(max_length=50)
    change_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.report} - {self.change_type} at {self.timestamp}"


class PeriodicReport(models.Model):
    REPORT_FREQUENCY_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ]
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name='periodic_reports',
        )
    frequency = models.CharField(
        max_length=10,
        choices=REPORT_FREQUENCY_CHOICES,
        )
    last_sent_at = models.DateTimeField(
        null=True,
        blank=True,
        )

    def __str__(self):
        return f"{self.get_frequency_display()} report for {self.report}"
