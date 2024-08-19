from django.contrib import admin
from .models import Post, Author, Tag, Comment


# Admin configuration for the Post model
class PostAdmin(admin.ModelAdmin):
    # filtering posts
    list_filter = ("author", "tags", "date")
    # Specifies the fields to be displayed in the list view of posts
    list_display = ("title", "author", "date")
    # Automatically populates the slug field based on the title when creating a new post.
    prepopulated_fields = {"slug": ["title"]}


# Admin configuration for the Comment model.
class CommentsAdmin(admin.ModelAdmin):
    # Specifies the fields to be displayed in the list view of posts
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentsAdmin)
