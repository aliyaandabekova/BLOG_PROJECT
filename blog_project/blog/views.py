from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .permissions import *
from .serializers import *
from .models import *

class BlogViewSet(ViewSet):
    permission_classes = [BlogPermissions]
    serializer_class = BlogSerializer
    def list(self,request):
        blogs = Blog.objects.all()
        serializer = self.serializer_class(blogs,many=True)
        return Response(serializer.data,status=200)
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class CommentViewSet(ViewSet):
    permission_classes = [CommentPermissions]
    serializer_class = CommentSerializer
    def list(self,request,blog_id):
        blog = Blog.objects.get(id=blog_id)
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data,status=200)
    def create(self,request,blog_id):
        user = request.user
        blog = Blog.objects.get(id=blog_id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            text = serializer.data.get('text')
            Comment.objects.create(user=user,text=text,blog=blog)
            serializer1 = BlogDetailSerializer(blog)
            return Response(serializer1.data, status=201)
        return Response(serializer.errors,status=400)

