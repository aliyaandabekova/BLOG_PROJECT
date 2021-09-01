from .views import *
from django.urls import path

urlpatterns = [
    path('blogs/',BlogViewSet.as_view({
        'get':'list',
        'post':'create'
    }),name='blogs'),
    path('blog/<int:blog_id>/',BlogViewSet.as_view({
        'get':'retrieve',
        'delete':'destroy',
    }),name='delete_blog'),
    path('comments/<int:blog_id>/',CommentViewSet.as_view({
        'get':'list',
        'post':'create',
    }),name='comments')

]