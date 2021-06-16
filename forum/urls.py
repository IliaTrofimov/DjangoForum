from django.urls import path
from . import views


app_name = 'forum'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name='post_details'),
    path('<int:post_id>/new_msg', views.new_message, name='new_message'),
    path('new_post/', views.NewPostView.as_view(), name='new_post'),
    path('<int:msg_id>/msg_up/', views.vote_message,  name='msg_vote_up', kwargs={'inc': 1}),
    path('<int:msg_id>/msg_down/', views.vote_message,  name='msg_vote_down', kwargs={'inc': -1}),
    path('<int:post_id>/post_up/', views.vote_post, name='post_vote_up', kwargs={'inc': 1}),
    path('<int:post_id>/post_down/', views.vote_post,  name='post_vote_down', kwargs={'inc': -1}),
]
