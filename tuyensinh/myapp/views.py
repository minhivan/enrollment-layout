from bson import ObjectId
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SubjectCluster, Applicants, Registers, Majors
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.files.storage import FileSystemStorage
from django.db.models.expressions import RawSQL


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return redirect("admin_dash")
            messages.success(request, 'Login success')
            HttpResponse("Login successfully")
            return redirect("home")
        else:
            messages.error(request, 'Login failed')
            HttpResponse("Login failed")
            return redirect("login")
    return render(request, 'account/sign-in.html', {})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repass = request.POST.get("re-password")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        full_name = first_name + " " + last_name
        if repass == password:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            messages.success(request, 'Account created successfully')
            applicant = Applicants()
            applicant.id = User.objects.get(username=username).pk
            applicant.email = email
            applicant.name = full_name
            applicant.save()
            HttpResponse("Created")
            return redirect("login")
        else:
            messages.error(request, 'Failed to create account')
            return redirect("register")
    return render(request, 'account/register.html', {})


def logout(request):
    auth.logout(request)
    return redirect("login")


# CLIENT DASHBOARD ONLY
def client_dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        username = request.user.get_username()
        user_id = User.objects.get(username=username).pk
        request_user = User.objects.get(id=user_id)
        check = Applicants.objects.filter(id=user_id)
        if check:
            applicant = Applicants.objects.get(id=user_id)
            admissions1 = Registers.objects.filter(user=user_id, status="pending")
            admissions2 = Registers.objects.filter(user=user_id, status="submitted")
            majors1 = []
            majors2 = []
            for admission in admissions1:
                major_label = admission.meta_data
                major = Majors.objects.get(label=major_label['Major'])
                majors1.append(major)
            for admission in admissions2:
                major_label = admission.meta_data
                major = Majors.objects.get(label=major_label['Major'])
                majors2.append(major)
            data1 = zip(admissions1, majors1)
            data2 = zip(admissions2, majors2)
            context = {
                "user": user,
                "applicant": applicant,
                "data1": data1,
                "data2": data2,
                "admission": admissions1
            }
            return render(request, 'page/dashboard.html', context)
        else:
            return redirect("login")


def delete_admission(request, id):
    if request.method == "POST":
        username = request.user.get_username()
        user_id = User.objects.get(username=username).pk
        admissions = Registers.objects.filter(user=user_id)
        confirm = ""
        for admission in admissions:
            if admission.id == id:
                delete_field = Registers.objects.filter(id=id)
                print(delete_field)
                delete_field.delete()
                return redirect("account")
            else:
                messages.error(request, "Cannot delete this form")
    return redirect("account")


def submit_admission(request, id):
    if request.method == "POST":
        username = request.user.get_username()
        user_id = User.objects.get(username=username).pk
        admissions = Registers.objects.filter(user=user_id)
        confirm = ""
        for admission in admissions:
            if admission.id == id:
                submit_field = Registers.objects.get(id=id)
                submit_field.status = "submitted"
                submit_field.save()
                return redirect("account")
            else:
                messages.error(request, "Cannot submit this form")
    return redirect("account")


# END USER DASHBOARD

# USER ACTION
def update_info(request, id):
    if request.method == "POST":
        password = request.POST.get("password")
        repass = request.POST.get("re-password")
        student_name = request.POST.get("student_name")
        student_dob = request.POST.get("student_birth")
        student_gender = request.POST.get("student_gender")
        student_phone = request.POST.get("student_phone")
        student_id = request.POST.get("student_identify")
        student_address = request.POST.get("student_address")
        user = User.objects.get(id=id)
        applicant = Applicants.objects.get(id=id)

        if None not in (password, repass):
            if repass == password:
                user.password = password
                user.save()
        if None not in (student_dob, student_address,
                        student_gender, student_phone, student_id, student_name):
            applicant.dob = student_dob
            applicant.gender = student_gender
            applicant.phone = student_phone
            applicant.identity = student_id
            applicant.address = student_address
            applicant.name = student_name
            applicant.save()
            context = {
                "user": user,
                "applicant": applicant
            }
            messages.success(request, "Update success")
            HttpResponse("Updated")
            return redirect("account")
        else:
            messages.error(request, 'Failed to update account')
            HttpResponse("Updated")
            return redirect("account")


# Admission
def apply(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST" and request.FILES['score_image']:
            username = request.user.get_username()
            user_id = User.objects.get(username=username).pk
            user = User.objects.get(id=user_id)
            applicant = Applicants.objects.get(id=user_id)
            student_name = request.POST.get("student_name")
            student_dob = request.POST.get("student_birth")
            student_gender = request.POST.get("student_gender")
            student_phone = request.POST.get("student_phone")
            student_id = request.POST.get("student_identify")
            student_address = request.POST.get("student_address")
            # SCORE
            major = request.POST.get("nvong")
            major_obj = Majors.objects.get(label=major)
            subject_name = request.POST.get("thop")
            avg_scores = {}
            for i in range(0, 3):
                temp_name = "avg_score" + str(i)
                avg_score = request.POST.get("avg_score" + str(i))
                avg_name = request.POST.get("avg_name" + str(i))
                avg_scores[avg_name] = avg_score
            print(avg_scores)
            avg = request.POST.get("final_score")
            meta = {"Major": major, "subject_cluster": subject_name, "average_score": avg}
            my_file = request.FILES['score_image']
            fs = FileSystemStorage()
            file = fs.save(my_file.name, my_file)
            uploaded_file_url = fs.url(file)
            apply_form = Registers(user=applicant, status="pending", result="waiting", meta_data=meta, details=avg_scores, image=file)
            apply_form.save()
            messages.success(request, 'Upload success')
            context = {
                "user": user,
                "applicant": applicant
            }
            HttpResponse("Updated")
            return render(request, 'apply.html', context)
        else:
            username = request.user.get_username()
            user_id = User.objects.get(username=username).pk
            user = User.objects.get(id=user_id)
            applicant = Applicants.objects.get(id=user_id)
            context = {
                "user": user,
                "applicant": applicant
            }
            return render(request, 'apply.html', context)


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
    subject_names = request.POST.get("subject").split(',')
    sub = {}
    index = 1
    for subject_name in subject_names:
        sub["Subject_" + str(index)] = subject_name
        index += 1
    name = request.POST.get("name")
    label = request.POST.get("label")
    detail = request.POST.get("detail")
    subject_cluster = SubjectCluster(name=name, detail=detail, subject=sub, label=label)
    subject_cluster.save()
    return HttpResponse("Inserted")


@csrf_exempt
def add_major(request):
    if request.method == "POST":
        subject_names = request.POST.get("subject_id").split(',')
        sub = {}
        index = 1
        for subject_name in subject_names:
            sub["cluster_" + str(index)] = subject_name
            index += 1
        name = request.POST.get("name")
        label = request.POST.get("label")
        detail = request.POST.get("detail")
        major = Majors(name=name, detail=detail, subject_id=sub, label=label)
        major.save()
        return HttpResponse("Inserted")


# ADMIN

def index_dash(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            admissions = Registers.objects.all()
            context = {
                "admissions": admissions
            }
    return render(request, 'admin/admindash.html', context)


def user(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            users = User.objects.all()
            context = {
                "users": users,
            }
            return render(request, 'admin/page/user.html', context)


def profile_user(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            request_user = User.objects.get(id=id)
            check = Applicants.objects.filter(id=id)
            if check:
                applicant = Applicants.objects.get(id=id)
                context = {
                    "applicant": applicant,
                    "request_user": request_user
                }
                if request.method == "POST":
                    password = request.POST.get("password")
                    repass = request.POST.get("re-password")
                    first_name = request.POST.get("firstname")
                    last_name = request.POST.get("lastname")
                    phone = request.POST.get("phone")
                    if repass == "":
                        request_user.first_name = first_name
                        request_user.last_name = last_name
                        request_user.save()
                        applicant.phone = request.POST.get("phone")
                        applicant.address = request.POST.get("address")
                        applicant.dob = request.POST.get("dob")
                        applicant.save()
                        messages.success(request, "Success")
                        return redirect("profile_user", id)
                    else:
                        if repass == password:
                            request_user.first_name = first_name
                            request_user.last_name = last_name
                            request_user.password = password
                            request_user.save()
                            applicant.phone = request.POST.get("phone")
                            applicant.address = request.POST.get("address")
                            applicant.dob = request.POST.get("dob")
                            applicant.save()
                            messages.success(request, "Success")
                            return redirect("profile_user", id)
                        else:
                            messages.error(request, "Cannot update")
                            return redirect("profile_user", id)
            else:
                context = {
                    "request_user": request_user
                }

    return render(request, 'admin/page/profile.html', context)


def delete_user(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            request_user = User.objects.filter(id=id)
            request_applicant = Applicants.objects.filter(id=id)
            if request_applicant:
                request_applicant.delete()
            request_user.delete()
    return redirect("admin_list_user")


def admission_list(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            admissions = Registers.objects.all()
            context = {
                "admissions": admissions
            }
            return render(request, 'admin/page/admission_list.html', context)
        else:
            return redirect("login")


def admission_detail(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            check = Registers.objects.filter(id=id)
            if check:
                admissions = Registers.objects.get(id=id)
                major = Majors.objects.get(label=admissions.meta_data['Major'])
                context = {
                    "admissions": admissions,
                    "major": major
                }
                return render(request, 'admin/page/admission-detail.html', context)
            else:
                return redirect("admission_list")
        else:
            return redirect("login")


def major_list(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            major = Majors.objects.all()
            context = {
                "majors": major
            }
            return render(request, 'admin/page/majors_list.html', context)
        else:
            return redirect("login")


def major_detail(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.user.is_superuser:
            check = Majors.objects.filter(id=id)
            if check:
                major = Majors.objects.get(id=id)
                label = major.label
                print(label)
                admissions = Registers.objects.filter(meta_data={'Major': label}, status="submitted")
                context = {
                    "major": major,
                    "admissions": admissions
                }
                if request.method == "POST" and 'update_major' in request.POST:
                    major = Majors.objects.get(id=id)
                    major.name = request.POST.get("name")
                    major.label = request.POST.get("label")
                    major.target_amount = request.POST.get("target_amount")
                    major.date_expired = request.POST.get("date_expired")
                    major.score_base = request.POST.get("score_base")
                    major.save()
                    return redirect("major_detail", id)
                if request.method == "POST" and 'result_major' in request.POST:
                    target = major.target_amount
                    score_base = major.score_base
                    list = {}
                    for admission in admissions:
                        user_score = admission.meta_data['average_score']
                        if score_base <= float(user_score):
                            list[admission.id] = float(user_score)
                        else:
                            admission.result = "failed"
                            admission.save()
                    if list:
                        sort_list = sorted(list.items(), key=lambda x: x[1], reverse=True)
                        print(sort_list)
                        count = 0
                        for i in sort_list:
                            if count < target-1:
                                print(i[0])
                                k = admissions.get(id=i[0])
                                print(k)
                                k.result = "passed"
                                k.save()
                                count = count + 1
                            else:
                                k = admissions.get(id=i[0])
                                print(k)
                                k.result = "failed"
                                k.save()
                return render(request, 'admin/page/major-detail.html', context)
            else:
                return redirect("major_list")
        else:
            return redirect("login")


