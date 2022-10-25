from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from .models import Registration
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
import csv


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_firstname = request.POST['user_firstname']
        user_lastname = request.POST['user_lastname']
        user_phone = request.POST['user_phone']
        user_email = request.POST['user_email']
        user_gender = request.POST['user_gender']
        user_mode_of_info = request.POST['user_mode_of_info']
        user_first_time = request.POST['user_first_time']
        user_residence = request.POST['user_residence']
        user_arrival_day = request.POST['user_arrival_day']
        abroad = request.POST['abroad']
        if Registration.objects.filter(user_firstname=user_firstname, user_lastname=user_lastname).exists():
            messages.info(request, 'Sorry you have registered already')
            return redirect('index')
        elif len(user_phone) != 10:
            messages.info(request, "Your phone number should be 10 digits")
            return redirect('index')
        else:
            new_reg = Registration(
                user_firstname=user_firstname,
                user_lastname=user_lastname,
                user_phone=user_phone,
                user_email=user_email,
                user_gender=user_gender,
                user_mode_of_info=user_mode_of_info,
                user_first_time=user_first_time,
                user_residence=user_residence,
                user_arrival_day=user_arrival_day,
                abroad = abroad,
            )
            new_reg.save()
            return render(request, 'congrat.html')
    return render(request, 'register.html')
        
#creating csv file for download
def csvfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Desposition'] = 'attachment; filename=registrations.csv'
    
    #writing to the csv file
    writer = csv.writer(response)
    
    registrations = Registration.objects.all()
    
    #adding headings
    writer.writerow(['First name', 'Last name', 'Phone', 'Email', 'Gender', 'Mode of info', 'Appearance at programs', 'Residence', 'Arrival day', 'Abroad'])
    
    #Appending to the csv file 
    for reg in registrations:
        writer.writerow([reg.user_firstname, reg.user_lastname, reg.user_phone, reg.user_email, reg.user_gender, reg.user_mode_of_info, reg.user_first_time, reg.user_residence, reg.user_arrival_day, reg.abroad])
    return response

#dashboard
def dashboard(request):
    return render(request, 'dashboard.html')