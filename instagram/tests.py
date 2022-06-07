from django.test import TestCase
from .models import  Image, Comments, Likes, Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='edgar',
            last_name='obare'
        )
        Profile.objects.create(
            bio='test bio',
            profile_photo='static/img/homepage.jpg',
            user_id=user.id
        )

    def test_bio(self):
        profile = Profile.objects.get(bio='test bio')
        self.assertEqual(profile.bio, 'test bio')

class LikesTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='edgar',
            last_name='obare'
        )
        image = Image.objects.create(
            image_caption='test post',
            image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
            profile_id=user.id,
            user_id=user.id
        )
        Likes.objects.create(
            image_id=image.id,
            user_id=user.id
        )
class ImageTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='edgar',
            last_name='obare'
        )
        Image.objects.create(
            image_name='test_image',
            image='https://akm-img-a-in.tosshub.com/indiatoday/images/story/202108/Instagram_0.jpg?ZZLGdE1PjohTO.aeUOUEQYBxAWLPgCGT&size=770:433',
            image_caption='test image',
            profile_id=user.id,
            user_id=user.id
        )

class CommentsTestCase(TestCase):
    def setUp(self):
        self.edgar=User(username = 'edgar', email='edgarobare@gmail.com', password='edgarobare')
        self.profile=Profile(bio='bio', user=self.edgar),
        self.comment=Comments(comment='bandana news network', user=self.edgar),

    def tearDown(self):
        Image.objects.all().delete
        Comments.objects.all().delete
    
    def test_save_method(self):
        self.comment.save_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) > 0)