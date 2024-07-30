from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.single_post, name='single-post-page')
]
