from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = "testuser",
            email = "tsetuseremail@test.com",
            password = "secret"
        )

        cls.post = Post.objects.create(
            title = "test blog title",
            body = "Some nice content",
            author = cls.user
        )


    def test_post_model(self):
        self.assertEqual(self.post.title, "test blog title"),
        self.assertEqual(self.post.body, "Some nice content")
        self.assertEqual(self.post.author.username,"testuser")
        self.assertEqual(str(self.post), "test blog title")
        self.assertEqual(self.post.get_absolute_url(),("/post/1/"))

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_detail_page_url_correct_location(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code,200)

    def test_postlist_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Some nice content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_detail_post_view(self):
        response = self.client.get(reverse('post_detail',
                                   kwargs={"pk":self.post.pk}))
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Some nice content')
        self.assertTemplateUsed(response, 'post_detail.html')