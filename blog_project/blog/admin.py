from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','text','date_created']
    readonly_fields = ['date_created']
admin.site.register(Blog,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','blog','date_created']
    readonly_fields = ['date_created']
admin.site.register(Comment,CommentAdmin)
