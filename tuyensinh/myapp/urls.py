from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # CLIENT
    path('', views.index, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('apply', views.apply, name="apply"),
    path('method/', views.method),
    path('method/direct/', views.direct),
    path('method/graduate/', views.graduate),
    path('method/profile/', views.checkProfile),
    path('method/highquality/', views.highQuality),
    path('method/fostering/', views.fostering),
    path('method/pedagogy/', views.pedagogy),
    path('user/dashboard/', views.client_dashboard, name="account"),
    path('user/dashboard/update/<int:id>', views.update_info),
    # API
    path('myapp/v1/addsubjectCluster/', views.add_subject),
    path('myapp/v1/update/<int:id>', views.update_info),
    path('myapp/v1/addmajor/', views.add_major),
    path('myapp/v1/user/admission/delete/<int:id>/', views.delete_admission, name="delete_admission"),
    path('myapp/v1/user/admission/submit/<int:id>/', views.submit_admission, name="submit_admission"),
    # ADMIN
    path('dashboard/', views.index_dash, name="admin_dash"),
    path('dashboard/user/list/', views.user, name="admin_list_user"),
    path('dashboard/user/profile/<int:id>/', views.profile_user, name="profile_user"),
    path('dashboard/user/delete/<int:id>/', views.delete_user, name="delete_user"),
    path('dashboard/admission/list/', views.admission_list, name="admission_list"),
    path('dashboard/admission/<int:id>/', views.admission_list, name="admin_list_choice"),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
