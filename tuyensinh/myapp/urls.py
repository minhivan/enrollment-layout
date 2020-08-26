from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('apply', views.apply),
    path('method/', views.method),
    path('method/direct', views.direct),
    path('method/graduate', views.graduate),
    path('method/profile', views.checkProfile),
    path('method/highquality', views.highQuality),
    path('method/fostering', views.fostering),
    path('method/pedagogy', views.pedagogy),
    path('user/dashboard', views.clientDashboard),
]
