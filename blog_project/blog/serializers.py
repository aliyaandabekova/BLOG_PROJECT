from .models import *
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()

class BlogDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Blog
        fields = ['title','text','date_created','comment_set']
