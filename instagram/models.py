from django.db import models
from cloudinary.models import CloudinaryField 
import datetime as dt
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    image_date = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def search_by_image_name(cls, search_term):
        images = cls.objects.filter(
            image_name__icontains=search_term)
        return images

    @classmethod
    def get_single_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    def __str__(self):
        return self.image_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def __str__(self):
        return self.user.username

class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    likes = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.likes

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-comment_date']

class Follow(models.Model): 
    posted = models.DateTimeField(auto_now_add=True)
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_followed')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_following')

    def __str__(self):
        return self.pk 