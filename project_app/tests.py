from django.test import TestCase
from .models import Post, AppUser

# Create your tests here.


class PostTestCase(TestCase):
    def testPost(self):
        user = AppUser.objects.create(username='username',
            password='password',
            email='mail@example.com',
            phone_number='1234567890',
            bio='Your bio goes here',
            is_organizer=True,
            is_artist=False,
        )
        post = Post(file="./data/events/event1.jpg", description="Blurb", date='15.01.2023 20:00:00', author=user)
        self.assertEqual(post.author, user)
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.date, "15.01.2023 20:00:00")
