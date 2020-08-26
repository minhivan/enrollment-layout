from bson import ObjectId
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SubjectCluster,Posts


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'sign-in.html', {})


def register(request):
    return render(request, 'register.html', {})


def clientdashboard(request):
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


# API
@csrf_exempt
def add_subject(request):
    subject = request.POST.get("subject")
    name = request.POST.get("name")
    label = request.POST.get("label")
    detail = request.POST.get("detail")
    subject_cluster = SubjectCluster(name=name, detail=detail, subject=subject, label=label)
    subject_cluster.save()
    return HttpResponse("Inserted")


@csrf_exempt
def add_post(request):
    comment = request.POST.get("comment").split(",")
    tags = request.POST.get("tags").split(",")
    user_details = {"first_name":request.POST.get("first_name"),"last_name":request.POST.get("last_name")}
    post = Posts(post_title=request.POST.get("post_title"),post_description=request.POST.get("post_description"),comment=comment,tags=tags,user_details=user_details)
    post.save()
    return HttpResponse("Inserted")

# FORM
