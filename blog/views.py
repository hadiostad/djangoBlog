from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

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


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/single-post.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("single-post-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form
        }
        return render(request, "blog/single-post.html", context)


class AddFavouriteView(View):
    def get(self, request):
        favourite_posts = request.session.get("favourite_posts")
        context = {}
        if favourite_posts is None or len(favourite_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=favourite_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/favourite-posts.html", context)

    def post(self, request):
        favourite_posts = request.session.get("favourite_posts")

        if favourite_posts is None:
            favourite_posts = []
            print("hi")

        post_id = int(request.POST["post_id"])

        if post_id not in favourite_posts:
            favourite_posts.append(post_id)
            request.session["favourite_posts"] = favourite_posts

        else:
            favourite_posts.remove(post_id)

        return HttpResponseRedirect("/")
