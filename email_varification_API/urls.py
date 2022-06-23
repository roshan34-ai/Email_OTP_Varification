from django.contrib import admin
from django.urls import path
from email_App.views import UserRegister, Varify_otp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegister.as_view(), name='register'),
    path('varify/', Varify_otp.as_view(), name='varify'),
]

