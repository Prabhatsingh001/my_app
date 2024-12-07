from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Hompepage(request):
    return HttpResponse("this is my homepage")


def registration(request):
    pass


def user_login(request):
    pass


def Dashboard(request):
    pass

