from django.shortcuts import render
from . models import Contact,User
import random,requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def  about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        Contact.objects.create(
            name = request.POST['name'],
            mobile = request.POST['mobile'],
            email = request.POST['email'],
            message = request.POST['message'],
        )
        msg = " Message Send Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['email'] = user.email
            request.session['name'] = user.name
            msg = " Login Successfull ! "
            return render(request,'appointment.html',{'msg':msg})
        except:
            msg1 = "Email or Password is incorrect"
            return render(request,'login.html',{'msg1':msg1})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg1 = " Email Already Registered! PLease Login"
            return render(request,'login.html',{'msg1':msg1})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                user=User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                )
                msg = " Account Created Succesfully ! "
                return render(request,'login.html',{'msg':msg})
            else:
                msg1 = " Password and Confirm Password deos not match"
                return render(request,'signup.html',{'msg1':msg1})
    else:
        return render(request,'signup.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['name']
        msg = " Logout Successfully ! "
        return render(request,'login.html',{'msg':msg})  # Redirect to the 'login' URL name
    # return render(request,'login.html',{'msg2':msg2})
    except:
        return render(request,'login.html')

def forgot_password(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        try:
            user = User.objects.get(mobile=mobile)
            otp = random.randint(1000,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"eYLHjNJ923XdpuOB7gqnTlVPD5FzEUwQ6abGAkR0McrKSIvWimqiMTAY02jxVCHLf8rUQ5BnsJ4PX3Nb","variables_values":str(otp),"route":"otp","numbers":user.mobile}

            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            return render(request,'verify_otp.html',{'otp':otp,'mobile':mobile})
        except:
            msg1=" Mobile Not Registered"
            return render(request,'forgot_password.html',{'msg1':msg1})
    else:
        return render(request,'forgot_password.html')

def verify_otp(request):
    if request.method=="POST":
        mobile=request.POST['mobile']
        otp=request.POST['otp']
        uotp=request.POST['uotp']
        if otp==uotp:
            return render(request,'new_password.html',{'mobile':mobile})
        else:
            msg1=" Enter Valid Otp !"
            return render(request,'verify_otp',{'msg1':msg1})
    else:
        return render(request,'verify_otp.html')
    
def new_password(request):
    if request.method=="POST":
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if cpassword==password:
                user = User.objects.get(mobile=request.POST['mobile'])
                user.password=password
                user.save()
                msg=" Password Changed Successfully! Login Now."
                return render(request,'login.html',{'msg':msg})
        else:
                msg=" Passwords Do not Match!"
                return render(request,'new_password.html',{'msg':msg})
    else:
        return render(request,'new_password.html')


def departments(request):
    return render(request,'departments.html')

def doctors(request):
    return render(request,'doctors.html')

def ourservice(request):
    return render(request,'ourservice.html')

def appointment(request):
    return render(request,'appointment.html')