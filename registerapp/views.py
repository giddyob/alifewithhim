from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from .models import Registration
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
import csv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required



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
        coming_with_kids = request.POST['coming_with_kids']
        num_of_kids = request.POST['num_of_kids']
        if Registration.objects.filter(user_firstname=user_firstname, user_lastname=user_lastname).exists():
            messages.info(request, 'Sorry you have registered already')
            return redirect('register')
        elif len(user_phone) != 10:
            messages.info(request, "Your phone number should be 10 digits")
            return redirect('register')
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
                coming_with_kids = coming_with_kids,
                num_of_kids = num_of_kids,
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
    writer.writerow(['First name', 'Last name', 'Phone', 'Email', 'Gender', 'Mode of info', 'Appearance at programs', 'Residence', 'Arrival day', 'Abroad', 'Coming with kid', 'Number of kids,'])
    
    #Appending to the csv file 
    for reg in registrations:
        writer.writerow([reg.user_firstname, reg.user_lastname, reg.user_phone, reg.user_email, reg.user_gender, reg.user_mode_of_info, reg.user_first_time, reg.user_residence, reg.user_arrival_day, reg.abroad, reg.coming_with_kids, reg.num_of_kids,])
    return response

#dashboard
@login_required(login_url="admin_login")
def dashboard(request):
    query = Registration.objects.all
    total_reg = reg_total()
    total_verified = verified_total()
    total_unverified = unverified_total()
    context = {
        'query':query,
        'total_reg':total_reg,
        'total_verified':total_verified,
        'total_unverified':total_unverified,
    }
    return render(request, 'admin.html', context)

def verified(request):
    query = Registration.objects.all
    total_reg = reg_total()
    total_verified = verified_total()
    total_unverified = unverified_total()
    context = {
        'query':query,
        'total_reg':total_reg,
        'total_verified':total_verified,
        'total_unverified':total_unverified,
    }
    return render(request, 'verified.html', context)

def unverified(request):
    query = Registration.objects.all
    total_reg = reg_total()
    total_verified = verified_total()
    total_unverified = unverified_total()
    context = {
        'query':query,
        'total_reg':total_reg,
        'total_verified':total_verified,
        'total_unverified':total_unverified,
    }
    return render(request, 'unverified.html', context)

def verify(request, rg_id):
    registration = Registration.objects.get(id=rg_id)
    registration.verified = True
    registration.save()
    messages.success(request, "You have been succesfully verified")
    return redirect('verification')

def admin_verify(request, reg_id):
    registration = Registration.objects.get(id=reg_id)
    registration.verified = True
    registration.save()
    return redirect('dashboard')


def about(request):
    return render(request, 'about.html')

def reg_total():
    registrations = Registration.objects.all()
    total_reg = 0
    for reg in registrations:
        total_reg += 1
    return total_reg

def verified_total():
    registrations = Registration.objects.all()
    total_verified = 0
    for reg in registrations:
        if reg.verified:
            total_verified +=1
    return total_verified

def unverified_total():
    registrations = Registration.objects.all()
    total_unverified = 0
    for reg in registrations:
        if reg.verified == False:
            total_unverified +=1
    return total_unverified

def unverify(request, reg_id):
    registration = Registration.objects.get(id=reg_id)
    registration.verified = False
    registration.save()
    return redirect('verified')


def verification(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(user_firstname__icontains=q) | Q(user_lastname__icontains=q))
        query = Registration.objects.filter(multiple_q)
    else:
        query = []
    total_reg = reg_total()
    total_verified = verified_total()
    total_unverified = unverified_total()
    context = {
        'query':query,
        'total_reg':total_reg,
        'total_verified':total_verified,
        'total_unverified':total_unverified,
    }
    return render(request, 'search.html', context)

def page_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('page-register')
    return render(request, 'admin-reg.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('admin_login')
    else:
        return render(request, 'admin-login.html')
    

def user_logout(request):
    logout(request)
    return redirect("admin_login")
        

def reg_delete(request, reg_id):
    registration = Registration.objects.filter(id=reg_id)
    registration.delete()
    return redirect("verified")