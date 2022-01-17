from celery import shared_task
from django.core.mail import send_mail
from .models import MyUser


@shared_task
def save_email():
    queryset = MyUser.objects.all()
    with open('result.txt', 'w', encoding='utf-8') as f:
        for item in queryset:
            f.write(item.email + '\n')


@shared_task
def send_mail_task(subject, text, email):
    send_mail(subject, text, 'no-reply@learnlanguage.com', [email], fail_silently=False)
