from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm


# A class-based view for the main page
class MainPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]  # Order posts by descending date
    context_object_name = "posts"  # Name for the list of posts in the template

    def get_queryset(self):
        queryset = super().get_queryset()
        item = queryset[:3]  # return only the first 3 posts
        return item


# A class-based view for the all posts page
class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    ordering = ["-date"]  # Order posts by descending date
    context_object_name = "all_posts"  # Name for the list of all posts in the template


# A class-based view for displaying a single post detail page
class PostDetailView(View):
    def add_favourite_posts(self, request, post_id):
        # Checks if a post is marked as favorite in the user's session
        favourite_posts = request.session.get("favourite_posts")
        if favourite_posts is not None:
            is_favourite_posts = post_id in favourite_posts
        else:
            is_favourite_posts = False
        return is_favourite_posts

    def get(self, request, slug):
        # Handles GET requests for a single post detail page

        # Retrieves the post based on the slug, creates the context dictionary with post details,
        # comment form, comments, and favorite status, and renders the template.
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "favourite": self.add_favourite_posts(request, post.id)
        }
        return render(request, "blog/single-post.html", context)

    def post(self, request, slug):
        # Handles POST requests for a single post detail page
        post = Post.objects.get(slug=slug)
        # Creates a comment form instance
        comment_form = CommentForm(request.POST)
        # validates comment, saves the comment
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # if valid, redirects the user back to the same post detail page
            return HttpResponseRedirect(reverse("single-post-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "favourite": self.add_favourite_posts(request, post.id)
        }
        return render(request, "blog/single-post.html", context)


# A class-based view for handling favorite posts
class AddFavouriteView(View):
    def get(self, request):
        # Handles GET requests for the favorite posts page

        # Retrieves favorite post IDs from the user's session, fetches the corresponding posts,
        # and creates the context dictionary with the list of favorite posts

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
        # Handles GET requests for the favorite posts page

        # Retrieves the current favorite post IDs from the user's session
        favourite_posts = request.session.get("favourite_posts")
        # Extracts the post ID from the submitted form data
        post_id = int(request.POST["post_id"])

        if favourite_posts is None:
            favourite_posts = []

        # If the post ID is not currently in the list
        if post_id not in favourite_posts:
            favourite_posts.append(post_id)

        else:
            favourite_posts.remove(post_id)

        # Updates the user's session
        request.session["favourite_posts"] = favourite_posts
        return HttpResponseRedirect("#")
