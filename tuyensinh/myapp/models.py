from django.db import models
from djongo import models

# Create your models here.


class Applicants(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=2)
    pob = models.CharField(max_length=255)
    nation = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=12)
    identity = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    wards = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name


class SubjectCluster(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    subject = models.JSONField()
    label = models.CharField(max_length=10)
    objects = models.DjongoManager()


class Majors(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=100)
    label = models.CharField(max_length=10)
    subject_id = models.JSONField()
    objects = models.DjongoManager()

    def item(self, i):
        return self[i]

    def __str__(self):
        return self.name


class Registers(models.Model):
    user = models.IntegerField()
    result = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    meta_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.JSONField()
    image = models.ImageField(upload_to='images/', default="")
    objects = models.DjongoManager()
