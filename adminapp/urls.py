from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.admin_logout,name='admin_logout'),
    path('users/',views.users,name='admin_users'),
    path('doctors/',views.doctors,name='admin_doctors'),
    path('appointments/',views.appointments,name='admin_appointments'),
    path('profiles/',views.profiles,name='admin_profiles'),
    path('contacts/',views.contacts,name='admin_contacts'),
    path('delete/<int:pk>/',views.delete_doctor,name='delete_doctor'),
]
