from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import email_id

from .forms import RegisterForm, LoginForm, BloodForm

def index(request):
    return render(request,"index.html")
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if (register_form.is_valid()):
            user_mail = register_form.cleaned_data['email']
            mail_id = email_id.objects.filter(mail_id =user_mail) 
            if len(mail_id) == 1:
                user = register_form.save()
                return redirect('login')
            else:
            # # return HttpResponse("Invalid data, Try again")
                messages.error(request, "Invalid data Try again")
                return redirect('einvalid')
                print(register_form)
        else:
            # return HttpResponse("Invalid data, Try again")
            messages.error(request, "Invalid data Try again")
            return redirect('invalid')
    #Creating the forms
    register_form = RegisterForm()
    context = {
        'register_form' : register_form,
        'title' : "Register as Candidate",
    }
    return render(request, 'booking.html', context)

# Login View
def loginView(request):
    # View for login page
    login_form = LoginForm(request)
    if request.method == 'POST':
        login_form = LoginForm(data = request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    return redirect('userpage')
        else:
             messages.error(request, "Invalid username or password.")
    context = {
            'login_form' : login_form,
            'title'      : 'Login',
    }
    return render(request, 'login.html', context)

# Logout View
def logoutView(request):
    logout(request)
    # messages.info(request, "Logged out successfully.")
    return redirect('home')
# Create your views here.

def userpage(request):
    return render(request,'userpage.html')



def invalidView(request):
    return render(request,'invalid.html')

def einvalidView(request):
    return render(request,'emailinvalid.html')

def requestView(request):
    breq_form=BloodForm
    if request.method == 'POST':
        breq_form = BloodForm(data = request.POST)
        if breq_form.is_valid():
          bloodrequest = breq_form.save()
          bloodrequest.p_reqstudent=request.user
          bloodrequest.save()
          return redirect('register')
        else:
             messages.error(request, "Invalid request")
    context = {
        'breq_form' : breq_form,
        'title' : "Request for blood",
    }  
    return render(request,'register.html',context)