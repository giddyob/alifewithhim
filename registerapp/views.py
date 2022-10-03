from django.shortcuts import render
from .models import Registration
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_email = request.POST['user_email']
        user_gender = request.POST['user_gender']
        user_mode_of_info = request.POST['user_mode_of_info']
        user_first_time = request.POST['user_first_time']
        user_residence = request.POST['user_residence']
        user_arrival_day = request.POST['user_arrival_day']
        if Registration.objects.filter(user_name=user_name).exists():
            messages.info(request, 'Sorry you have registered already')
            return redirect('index')
        else:
            new_reg = Registration(
                user_name=user_name,
                user_phone=user_phone,
                user_email=user_email,
                user_gender=user_gender,
                user_mode_of_info=user_mode_of_info,
                user_first_time=user_first_time,
                user_residence=user_residence,
                user_arrival_day=user_arrival_day,
            )
            new_reg.save()
            return render(request, 'congrat.html')
