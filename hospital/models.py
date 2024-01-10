from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.PositiveIntegerField()
    password = models.CharField(max_length=16)


    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female','Female')])
    age = models.PositiveSmallIntegerField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    address = models.TextField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pic/',default="")

    def __str__(self):
        return self.name



    
class appointment(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    check_app = models.BooleanField(default=False)


    def __str__(self):
        return self.patient.name

    

class patient_profile(models.Model):
    patient = models.ForeignKey(appointment,on_delete=models.CASCADE, default=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    disease = models.TextField()
    daignosis = models.TextField()
    age = models.PositiveSmallIntegerField(default=None)
    gender = models.CharField(max_length=10,default=None ,choices=[('Male','Male'),('Female','Female')])
    address = models.TextField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.patient.patient.name

