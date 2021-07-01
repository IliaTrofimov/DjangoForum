import datetime

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http.response import HttpResponseRedirect


from .models import Post, Message, MessageVote, PostVote
from .forms import MessageForm, PostForm


class IndexView(generic.ListView):
    paginate_by = 10
    template_name = 'forum/index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.order_by('-rating')


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST' and request.user.is_authenticated:
        form = MessageForm(request.POST)
        if form.is_valid():
            Message(text=form.cleaned_data['text'],
                    author=request.user,
                    root_post_id=post_id,
                    root_message_id=form.cleaned_data['reply_id'],
                    upload_date=datetime.datetime.now()).save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = MessageForm()

    return render(request,
                  'forum/post_details.html',
                  {'form': form, 'post': post, 'messages': post.get_answers()})


class NewPostView(generic.View):
    form_class = PostForm
    template_name = 'forum/new_post.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Post(text=form.cleaned_data['text'],
                 author=request.user,
                 title=form.cleaned_data['title'],
                 upload_date=datetime.datetime.now()).save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def vote_message(request, msg_id, inc: int):
    try:
        msg = Message.objects.get(pk=msg_id)
        MessageVote(user=request.user, message=msg, is_vote_up=(inc > 0)).save()
        msg.rating += inc
        msg.save()
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def vote_post(request, post_id, inc: int):
    try:
        post = Message.objects.get(pk=post_id)
        PostVote(user=request.user, post=post, is_vote_up=(inc > 0)).save()
        post.rating += inc
        post.save()
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def msg_delete(request, msg_id):
    try:
        msg = Message.objects.get(pk=msg_id)
        if msg.author == request.user or request.user.is_superuser:
            msg.delete()
    except Message.DoesNotExist:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def post_delete(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        if post.author == request.user or request.user.is_superuser:
            post.delete()
    except Post.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('forum:index'))
