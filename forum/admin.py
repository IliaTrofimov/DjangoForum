from django.contrib import admin

from .models import Message, Post, PostVote, MessageVote

admin.site.register(Message)
admin.site.register(Post)
admin.site.register(PostVote)
admin.site.register(MessageVote)
