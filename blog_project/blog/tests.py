from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from .models import *
from django.urls import reverse

class BlogTesCase(APITestCase):
    def setUp(self) -> None:
        self.admin = User.objects.create_user(username='admin',password='1234')
        self.group = Group.objects.create(name='admin')
        self.admin.groups.add(self.group)
        self.blog = Blog.objects.create(title='Math',text='1+1')
    def test_get_blogs(self):
        self.url = reverse('blogs')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)
    def test_create_blog(self):
        self.client.login(username='admin',password='1234')
        self.url = reverse('blogs')
        data = {'title':'Math','text':'how much?'}
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)
