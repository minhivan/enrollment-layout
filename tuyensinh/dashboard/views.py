from bson import ObjectId
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.models import SubjectCluster, Applicants, Registers, Majors
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage
# Create your views here.


def indexdash(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            admissions = Registers.objects.get().all()

    return render(request, 'admindash.html', {})


def user(request):
    return render(request, 'page/user.html', {})


def profile_user(request):
    return render(request, 'page/profile.html', {})


def listchoice(request):
    return render(request, 'page/list-choice.html', {})
