from django.urls import path
from . import views  


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('csvfile', views.csvfile, name='csvfile'),
    path('verify', views.verify, name='verify'),
    path('about', views.about, name='about'),
    path('verify/<int:reg_id>', views.verify, name='verify'),
    path('unverify/<int:reg_id>', views.unverify, name='unverify'),
    path('verified', views.verified, name='verified'),
    path('unverified', views.unverified, name='unverified'),
    path('verification', views.verification, name='verification'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('page_register', views.page_register, name="page-register")
]