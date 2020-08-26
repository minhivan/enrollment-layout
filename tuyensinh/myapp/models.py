from django.db import models
from djongo import models


# Create your models here.

class Applicants(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=2)
    pob = models.CharField(max_length=255)
    nation = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=12)
    identity = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    wards = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubjectCluster(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    subject = models.JSONField()
    label = models.CharField(max_length=10)
    objects = models.DjongoManager()

    def __str__(self):
        return self.label


class Majors(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=100)
    label = models.CharField(max_length=10)
    subject_id = models.JSONField()

    def __str__(self):
        return self.label


class Registers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    major_id = models.ForeignKey(Majors, on_delete=models.CASCADE)


class Results(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    register_id = models.ForeignKey(Registers, on_delete=models.CASCADE)
    score = models.JSONField()


class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Applicants, on_delete=models.CASCADE)
    action = models.JSONField()


class Posts(models.Model):
    _id = models.ObjectIdField()
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    comment = models.JSONField()
    tags = models.JSONField()
    user_details = models.JSONField()
    objects = models.DjongoManager()
