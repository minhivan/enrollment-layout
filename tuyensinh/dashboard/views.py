from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def indexdash(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, 'admindash.html', {})


def user(request):
    return render(request, 'page/user.html', {})


def profile_user(request):
    return render(request, 'page/profile.html', {})


def listchoice(request):
    return render(request, 'page/list-choice.html', {})
