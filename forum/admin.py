from django.contrib import admin

from .models import Message, Post

admin.site.register(Message)
admin.site.register(Post)

