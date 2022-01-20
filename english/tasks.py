from celery import shared_task
from django.core.mail import send_mail
from .models import MyUser


@shared_task
def send_mail_client(text, email):
    send_mail(subject='Письмо от компании',
              message=text,
              from_email='no-reply@learnlanguage.com',
              recipient_list=list(email),
              fail_silently=False)


@shared_task
def send_mail_company(text, email):
    send_mail(subject='Письмо от клиента',
              message=text,
              from_email=email,
              recipient_list=list('info@learnlanguage.com'),
              fail_silently=False)
