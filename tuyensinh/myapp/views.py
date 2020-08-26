from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'admindash.html', {})


def login(request):
    return render(request, 'sign-in.html', {})


def register(request):
    return render(request, 'register.html', {})


def clientDashboard(request):
    return render(request, 'page/dashboard.html', {})


def apply(request):
    return render(request, 'apply.html', {})


def method(request):
    return render(request, 'method.html', {})


# Method page
def direct(request):
    return render(request, 'page/method1.html', {})


def graduate(request):
    return render(request, 'page/method2.html', {})


def checkProfile(request):
    return render(request, 'page/method3.html', {})


def highQuality(request):
    return render(request, 'page/method4.html', {})


def fostering(request):
    return render(request, 'page/method5.html', {})


def pedagogy(request):
    return render(request, 'page/method6.html', {})
