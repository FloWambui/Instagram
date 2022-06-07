from django.contrib import admin
from .models import Image, Profile, Comments, Likes, Follow

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Follow)
