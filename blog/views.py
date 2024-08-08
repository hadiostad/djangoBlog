from django.shortcuts import render
from .models import Post


all_posts = Post.objects.all().order_by('-date')


def main_page(request):
    return render(request, 'blog/index.html', {
        "posts": all_posts
    })


def posts(request):
    return render(request, 'blog/posts.html', {
        "all_posts": all_posts
    })


def single_post(request, slug):
    recognized_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/single-post.html', {
        'post': recognized_post
    })
