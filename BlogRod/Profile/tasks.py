from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def mail_welcome_user(email):
    send_mail(
    'Bienvenido!',
    'Here is the message.',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)
