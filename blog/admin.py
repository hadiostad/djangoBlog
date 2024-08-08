from django.contrib import admin
from .models import Post, Author, Tag


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)
