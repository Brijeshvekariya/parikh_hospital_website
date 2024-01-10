from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from hospital.models import User as customuser
from hospital.models import Doctor,appointment,patient_profile,Contact
# Create your views here.
def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user  = User.objects.get(username = username)
            user=authenticate(username=username, password=password)
            if user and user.is_superuser:
                login(request,user)
                return redirect('dashboard')
            messages.error(request,"Username or Password is incorrect")
            return redirect('/')
        return render(request,'admin_login.html') 

    except Exception as e:
        print(e)
        return render(request,'admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect("admin_login")

def dashboard(request):
    flag = True
    return render(request,'admin_dashboard.html',{'flag':flag})

def users(request):
    user = customuser.objects.all()
    return render(request,'admin_dashboard.html',{"user" : user})


def doctors(request):
    try:
        doctor = Doctor.objects.all()
        return render(request,'admin_dashboard.html',{'doctor':doctor})
    except:
        return HttpResponse("No doctor found")  

def appointments(request):
    appoint = appointment.objects.all()
    return render(request,'admin_dashboard.html',{'appoint':appoint})
def profiles(request):
    profile = patient_profile.objects.all()
    return render(request,'admin_dashboard.html',{'profile':profile})
def contacts(request):
    people = Contact.objects.all()
    return render(request,'admin_dashboard.html',{'people':people})

def delete_doctor(request,pk):
    doctor = Doctor.objects.get(pk=pk)
    doctor.delete()
    return redirect('adminapp:doctors')