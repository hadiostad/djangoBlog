from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm


class Main_Page_View(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        item = queryset[:3]
        return item


class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/single-post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
