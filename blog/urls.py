from django.urls import path
from . import views


urlpatterns = [
    path('', views.Main_Page_View.as_view(), name='main-page'),
    path('posts', views.PostListView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='single-post-page')
]
