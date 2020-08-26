from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexdash),
    path('user/', views.user),
    path('profile/', views.profile_user),
    path('list/', views.listchoice),
]
