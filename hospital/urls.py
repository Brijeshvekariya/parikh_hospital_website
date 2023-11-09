
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
    path('user_profile/', views.user_profile, name="user_profile"),
    path('dr_index/', views.dr_index, name="dr_index"),
    path('dr_profile/', views.dr_profile, name="dr_profile"),

]