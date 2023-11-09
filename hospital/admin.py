from django.contrib import admin
from . models import Contact,User,Doctor,profile,appointment

# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(profile)
admin.site.register(appointment)