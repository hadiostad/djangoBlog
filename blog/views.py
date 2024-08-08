from django.shortcuts import render, get_object_or_404
from .models import Post


def main_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/posts.html', {
        "all_posts": all_posts
    })


def single_post(request, slug):
    recognized_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/single-post.html', {
        "post": recognized_post,
        "post_tags": recognized_post.tags.all()
    })