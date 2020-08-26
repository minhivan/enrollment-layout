from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexdash(request):
    return render(request, 'admindash.html', {})


def user(request):
    return render(request, 'page/user.html', {})


def profile_user(request):
    return render(request, 'page/profile.html', {})


def listchoice(request):
    return render(request, 'page/list-choice.html', {})
