from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic.list import MultipleObjectMixin

from .models import Post, Message
from .forms import MessageForm, PostForm


class IndexView(generic.ListView):
    paginate_by = 10
    template_name = 'forum/index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.order_by('-rating')


class DetailsView(DetailView, MultipleObjectMixin):
    model = Post
    paginate_by = 5
    template_name = 'forum/post_details.html'

    def get_context_data(self, **kwargs):
        object_list = Message.objects.filter(root_post=self.get_object())
        context = super(DetailsView, self).get_context_data(object_list=object_list, **kwargs)
        return context


class NewPostView(generic.View):
    form_class = PostForm
    template_name = 'forum/new_post.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        Post(text=request.POST['post_text'], title=request.POST['post_title'], author=request.POST['post_author']).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def vote_message(request, msg_id, inc: int):
    try:
        msg = Message.objects.get(pk=msg_id)
        msg.rating += inc
        msg.save()
    except Message.DoesNotExist:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def vote_post(request, post_id, inc: int):
    try:
        post = Post.objects.get(pk=post_id)
        post.rating += inc
        post.save()
    except Post.DoesNotExist:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def new_message(request, post_id):
    Message(text=request.POST['post_text'],
            author=request.POST['post_author'],
            root_post_id=post_id).save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
