"""gram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,include
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views as auth_views
from instagram import views 

app_name = "instagram"  

urlpatterns = [
   re_path('admin/', admin.site.urls),
   re_path('accounts/register/',
          RegistrationView.as_view(success_url='/'),
          name='django_registration_register'),
   re_path('accounts/', include('django_registration.backends.one_step.urls')),
   re_path('accounts/', include('django.contrib.auth.urls')),
   re_path('',include('instagram.urls')),
   re_path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/login.html'), name = 'logout'),
   re_path('password-change/', auth_views.PasswordResetView.as_view(), name='password_change'),
]
