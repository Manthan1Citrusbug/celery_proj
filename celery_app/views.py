from django.shortcuts import render
from django.http import HttpResponse
from .task import sleepy, send_an_email
# Create your views here.


def home(request):
    msg = sleepy.delay(5)
    send_an_email.delay('TestCase','This is Test Email',*["patelmanthan2905@gmail.com"])
    return HttpResponse("Email Send")