from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.
from .models import Post, Message


class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'best_posts_list'

    def get_queryset(self):
        """Returns ten best-rated posts."""
        return Post.objects.order_by('-rating')[:10]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'forum/post_details.html'
