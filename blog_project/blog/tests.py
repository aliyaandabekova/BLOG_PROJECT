from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from .models import *
from django.urls import reverse

class BlogTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='user',password='1234')
        self.admin = User.objects.create_user(username='admin',password='1234')
        self.group = Group.objects.create(name='admin')
        self.group1 = Group.objects.create(name='user')
        self.admin.groups.add(self.group)
        self.user.groups.add(self.group1)
        self.blog = Blog.objects.create(title='Math',text='1+1')
    def test_get_blogs(self):
        self.url = reverse('blogs')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)
    def test_create_blog_as_a_admin(self):
        self.client.login(username='admin',password='1234')
        self.url = reverse('blogs')
        data = {'title':'Math','text':'how much?'}
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)
    def test_create_blog_as_a_user(self):
        self.client.login(username='user',password='1234')
        self.url = reverse('blogs')
        data = {'title': 'Math', 'text': 'how much?'}
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code,403)


class CommentTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='user', password='1234')
        self.admin = User.objects.create_user(username='admin', password='1234')
        self.group = Group.objects.create(name='admin')
        self.group1 = Group.objects.create(name='user')
        self.admin.groups.add(self.group)
        self.user.groups.add(self.group1)
        self.blog = Blog.objects.create(title='Math', text='1+1')
    def test_get_comments_of_blog(self):
        self.url = reverse('comments',args=(self.blog.id,))
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)
    def test_create_comments_by_user(self):
        self.client.login(username='user',password='1234')
        self.url = reverse('comments',args=(self.blog.id,))
        data = {'text':'good'}
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code,201)
    def test_create_comments_by_admin(self):
        self.client.login(username='admin',password='1234')
        self.url = reverse('comments',args=(self.blog.id,))
        data = {'text':'good'}
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, 403)



