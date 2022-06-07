from django.urls import re_path, include
from . import views

urlpatterns=[
    re_path('^$',views.index,name = 'homepage'),
    re_path('user/<int:id>/', views.user_profile, name='user.profile'),
]