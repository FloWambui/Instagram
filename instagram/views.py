from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import  Image, Comments, Likes, Profile, User
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="django_registration/registration_form.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="index.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return render(request, 'registration/login.html')


@login_required
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