from django.contrib import admin
from . models import Contact,User,Doctor,appointment,patient_profile





# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(appointment)
admin.site.register(patient_profile)



