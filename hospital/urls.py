
from django.urls import path,include
from . import views  # import all views in this file

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('ourservice/', views.ourservice, name='ourservice'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('create_appointment/', views.create_appointment, name="create_appointment"),
    path('save_appointment/', views.save_appointment, name="save_appointment"),
    path('logout/', views.logout, name="logout"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('new_password/', views.new_password, name="new_password"),
    path('change_password/', views.change_password, name="change_password"),
    path('dr_index/', views.dr_index, name="dr_index"),
    path('dr_profile/', views.dr_profile, name="dr_profile"),
    path('check_appointment/', views.check_appointment, name="check_appointment"),
    path('check_app/<int:pk>/', views.check_app, name="check_app"),
    path('today_app/', views.today_app, name="today_app"),
    path('todays_patient/', views.todays_patient, name="todays_patient"),
    path('viewall/', views.viewall, name="viewall"),
    path('patient_name/', views.patient_name, name="patient_name"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('patient_viewprofile/<int:pk>/',views.patient_viewprofile, name='patient_viewprofile'),
    path('patient_editprofile/<int:pk>/',views.patient_editprofile, name='patient_editprofile'),
    path('patient_save/', views.patient_save, name="patient_save"),

]