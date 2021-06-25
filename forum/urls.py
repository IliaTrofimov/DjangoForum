from django.urls import path
from . import views


app_name = 'forum'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:post_id>/', views.post_view, name='post_details'),
    path('new_post/', views.NewPostView.as_view(), name='new_post'),
    path('<int:msg_id>/msg_up/', views.vote_message,  name='msg_vote_up', kwargs={'inc': 1}),
    path('<int:msg_id>/msg_down/', views.vote_message,  name='msg_vote_down', kwargs={'inc': -1}),
    path('<int:post_id>/post_up/', views.vote_post, name='post_vote_up', kwargs={'inc': 1}),
    path('<int:post_id>/post_down/', views.vote_post,  name='post_vote_down', kwargs={'inc': -1}),
    path('<int:msg_id>/msg_delete/', views.msg_delete,  name='msg_delete'),
    path('<int:post_id>/post_delete/', views.post_delete,  name='post_delete'),
]
