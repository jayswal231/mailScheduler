from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reminder_email(subject, message, recipient_email):
    send_mail(
        subject,
        message,
        'company@gmail.com',
        [recipient_email],
        fail_silently=False
    )