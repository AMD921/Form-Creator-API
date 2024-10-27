from celery import shared_task
from .models import PeriodicReport
from django.utils import timezone

@shared_task
def send_periodic_reports():
    reports = PeriodicReport.objects.filter(
        frequency='monthly',
        last_sent_at__lt=timezone.now() - timezone.timedelta(days=30)
    )
    for report in reports:
        # ارسال گزارش به صورت ایمیل یا هر عملیات دیگر
        print(f"Sending monthly report for {report.report}")
        report.last_sent_at = timezone.now()
        report.save()