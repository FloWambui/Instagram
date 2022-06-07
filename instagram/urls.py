from django.urls import re_path, include
from . import views

app_name= 'instagram'

urlpatterns=[
    re_path('^$',views.index,name = 'homepage'),
    re_path("register", views.register_request, name="register"),
    re_path("login", views.login_request, name="login"),
    re_path("logout", views.logout_request, name= "logout"),
    re_path('profile/update/', views.update_profile, name='update.profile'),
    re_path('profile/', views.profile, name='profile'),     
    re_path('upload/add/', views.save_image, name='save.image')
]