from django.urls import path
from . import views


urlpatterns = [
    # Maps the root URL to the main page view.
    path('', views.MainPageView.as_view(), name='main-page'),
    # Maps the posts list page to the PostListView.
    path('posts', views.PostListView.as_view(), name='posts-page'),
    # Maps a post detail page to the PostDetailView, capturing the post slug.
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='single-post-page'),
    # Maps the add favorite action to the AddFavouriteView.
    path('favourite', views.AddFavouriteView.as_view(), name="add-favourite")
]
