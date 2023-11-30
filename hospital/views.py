from django.shortcuts import render,redirect
from . models import Contact,User,Doctor,appointment,patient_profile
import random,requests
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

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
            return redirect('create_appointment')

        except:
            try:
                doctor = Doctor.objects.get(
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                request.session['email'] = doctor.email
                request.session['name'] = doctor.name
                msg = " Login Successfull ! "
                return render(request,'dr_index.html',{'msg':msg})
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
                name = request.POST['name']
                email = request.POST['email']
                mobile = request.POST['mobile']
                password = request.POST['password']
                subject = "Thank You for Registering with Us!"
                message = f"Dear {name},\n\n\tWe wanted to extend our heartfelt gratitude for choosing to register with us! Your decision to join our community means a lot to us. We are thrilled to have you on board and look forward to providing you with an exceptional experience. \n\n\tThank you for placing your trust in us. Should you have any questions or need assistance, please don not hesitate to reach out. We're here to ensure your journey with us is seamless and enjoyable. \n\n\tOnce again, thank you for becoming a part of Parikh Hospital. We cannot wait to begin this exciting journey together! \n\nWarm regards, \nParikh Hospital"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail( subject, message, email_from, recipient_list )
                User.objects.create(
                    name = name,
                    email = email,
                    mobile = mobile,
                    password = password,
                )
                msg = " Account Created Succesfully ! "
                return render(request,'login.html',{'email':email,'msg':msg})
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
            return render(request,'verify_otp.html',{'msg1':msg1})
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

def change_password(request):
    if request.method=="POST":
        user=User.objects.get(email=request.session['email'])   
        old_pass=request.POST['opassword']
        if user.password==old_pass:
            new_pass=request.POST['npassword']
            cpass = request.POST['cpassword']
            if new_pass==cpass:
                user.password= new_pass
                user.save()
                try:
                    del request.session["email"]
                    del request.session['name']  # remove the value from session dictionary by key name 'email'
                except KeyError:
                    msg1=" Error Occured ! PLease Change Password Again "
                    return render(request,'change_password.html',{'msg1':msg1}) 
                msg="Password changed successfully, Please login again to access your account."
                return render(request,'login.html',{'msg':msg})
            else:
                msg=" New and Confirm passwords do not match!"
                return render(request,'change_password.html',{'msg':msg})
        else:
            msg=" Old password is incorrect!"
            return render(request,'change_password.html',{'msg':msg})
    else:
        return render(request,'change_password.html')


    
# def patient_list(request):

def dr_index(request):
    return render(request,'dr_index.html')


def departments(request):
    return render(request,'departments.html')

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request,'doctors.html',{'doctors':doctors})

def ourservice(request):
    return render(request,'ourservice.html')

def create_appointment(request):
    user = User.objects.get(email = request.session['email'])
    doctors = Doctor.objects.all()
    today = datetime.now().date()
    return render(request, 'appointment.html', {'user': user, 'doctors': doctors, 'today':today,})

def save_appointment(request):
    if request.method == "POST":
        patient_username = request.POST['patient']
        doctor_name = request.POST['doctor']
        date = request.POST['date']
        time = request.POST['time']
        patient = None
        doctor = None
        try:
            patient = User.objects.get(name=patient_username)
            doctor = Doctor.objects.get(name=doctor_name)
            appointment.objects.get(patient=patient, doctor=doctor, date=date, time = time)
            msg1 = " Your Appointment is already booked!"
            return render(request, 'appointment.html', {'msg1': msg1})
        except appointment.DoesNotExist:
            msg = " Appointment created Successfully!"
            appointment.objects.create(
                patient=patient,
                doctor=doctor,
                date=date,
                time=time,
            )
            return render(request, 'appointment.html', {'msg': msg})
    else:
        return render(request, 'appointment.html')
    

def dr_profile(request):
    doctor = Doctor.objects.get(email = request.session['email'])
    if request.method=="POST":
        doctor.name = request.POST['name']
        doctor.specialization = request.POST['specialization']
        doctor.experience = request.POST['experience']
        doctor.education = request.POST['education']
        doctor.age = request.POST['age']
        doctor.phone = request.POST['phone']
        doctor.email = request.POST['email']
        doctor.address = request.POST['address']
        try:
            doctor.profile_pic = request.FILES['profile_pic']
        except:
            pass
        doctor.save()
        msg = " Profile Updated Successfully !"
        return render(request,'dr_index.html',{'doctor':doctor ,'msg':msg})
    else:
        return render(request,'dr_profile.html',{'doctor':doctor})

def check_appointment(request):
    doctor = Doctor.objects.get(email = request.session['email'])
    appointments = appointment.objects.filter(doctor = doctor).order_by('date')
    nopending = all(appointment.check_app for appointment in appointments)
    
    return render(request,'check_appointment.html',{'appointments':appointments,'nopending':nopending})

def check_app(request,pk):
    doctor = Doctor.objects.get(email = request.session['email'])
    if request.method=='POST':
        appoint = appointment.objects.get(pk=pk)
        appoint.check_app = True
        appoint.save()
    appointments = appointment.objects.filter(doctor = doctor).order_by('date')
    nopending = all(appointment.check_app for appointment in appointments)
    return render(request,'check_appointment.html',{'appointments':appointments,'nopending':nopending,'appoint':appoint})

def today_app(request):
    doctor = Doctor.objects.get(email = request.session['email'])
    if request.method=='POST':
        appointment_id = (request.POST['appointment_id']),
        appoint = appointment.objects.get(id = appointment_id)
        appoint.check_app = True
        appoint.save()
    today = datetime.now().strftime('%Y-%m-%d')
    appointments = appointment.objects.filter(doctor = doctor,date = today).order_by('time')
    
    
    return render(request,'today_appointment.html',{'appointments':appointments})

def todays_patient(request):
    today = datetime.now().strftime('%Y-%m-%d')
    doctor = Doctor.objects.get(email = request.session['email'])
    appointments = appointment.objects.filter(doctor = doctor, date = today).order_by('time')
    return render(request,'today_appointment.html',{'appointments':appointments})

def viewall(request):
    doctor = Doctor.objects.get(email = request.session['email'])
    appointments = appointment.objects.filter(doctor = doctor).order_by('date')
    return render(request,'viewall_app.html',{'appointments':appointments})


def patient_name(request):
    doctor = Doctor.objects.get(email = request.session['email'])
    appoint = appointment.objects.get(id = request.POST['app_id'])
    return render(request,"profile.html",{'appoint':appoint})


def user_profile(request):
    doctor = Doctor.objects.get(email=request.session['email'])

    if request.method == "POST":
        appoint_id = request.POST['appoint_id']
        appointer = appointment.objects.get(id = appoint_id)
        patient = request.POST['patient_name']  # If 'patient_name' exists, retrieve its value
        disease = request.POST['disease']
        diagnosis = request.POST['diagnosis']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']
        city = request.POST['city']
        patient_profile.objects.create(
            patient = appointer,
            doctor = doctor, 
            disease = disease,
            daignosis = diagnosis,
            age = age,
            gender = gender,
            address = address,
            city = city,
        )
        msg = "profile saved Successfully !"
        if appoint_id:
            appoint = appointment.objects.get(id = appoint_id)
            appoint.check_app = True
            appoint.save()
        appointments = appointment.objects.filter(doctor = doctor).order_by('date')
        nopending = all(appointment.check_app for appointment in appointments)
        return render(request,'check_appointment.html',{'appointments':appointments,'nopending':nopending,'appoint':appoint})
    else:
        return render(request, 'profile.html')
def patient_viewprofile(request,pk):
    appt = appointment.objects.get(pk=pk)
    patient = patient_profile.objects.get(patient=appt)
    return render(request,'patient_viewprofile.html',{'patient' : patient})

def patient_editprofile(request,pk):
    appt = appointment.objects.get(pk=pk)
    patient = patient_profile.objects.get(patient=appt)
    return render(request,'patient_editprofile.html',{"patient":patient})
    
def patient_save(request):
    patient_id = request.POST['id']
    patient = patient_profile.objects.get(id = patient_id)
    if patient:
        if request.method=="POST":
            patient.disease = request.POST['disease']
            patient.daignosis = request.POST['diagnosis']
            patient.age = request.POST['age']
            patient.gender = request.POST['gender']
            patient.address = request.POST['address']
            patient.city = request.POST['city']
            patient.save()
            msg = "Profile Updated Successfully"
            return render(request,'patient_editprofile.html',{"msg":msg})
        else:
            return render(request,'patient_editprofile.html')


# done project !