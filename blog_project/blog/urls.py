from .views import *
from django.urls import path

urlpatterns = [
    path('blogs/',BlogViewSet.as_view({
        'get':'list',
        'post':'create'
    }),name='blogs'),

]