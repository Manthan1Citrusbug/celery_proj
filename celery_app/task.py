from celery import shared_task
from time import sleep 
from django.core.mail import send_mail
from django.conf import settings

@shared_task()
def sleepy(duration):
    sleep(duration)
    return "Success!!"

@shared_task()
def send_an_email(subject,content,*to):
    print(type(to))
    send_mail(
        subject,
        content,
        settings.EMAIL_HOST_USER,
        to,
        fail_silently=False
    )
    return None