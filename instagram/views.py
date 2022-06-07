from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import  Image, Comments, Likes, Profile, User


def index(request):
    images = Image.objects.all().order_by('-image_date')
    return render(request, 'index.html', {'images': images})


def user_profile(request, id):
    # check if user exists
    if User.objects.filter(id=id).exists():
        # get the user
        user = User.objects.get(id=id)
        # get all the images for the user
        images = Image.objects.filter(user_id=id)
        # get the profile of the user
        profile = Profile.objects.filter(user_id=id).first()
        return render(request, 'user-profile.html', {'images': images, 'profile': profile, 'user': user})
    else:
        return redirect('/')