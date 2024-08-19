from django.db import models
from django.core.validators import MinLengthValidator


# Represents a tag for a blog post
class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        # Returns a string representation of the Tag
        return self.caption


# Represents an author of a blog post.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        # Returns a string representation of the first name and last name
        return f"{self.first_name} {self.last_name}"


# blog post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(50)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")  # One-to-many Relationship
    tags = models.ManyToManyField(Tag)  # Many-to-many relationships

    def __str__(self):
        # Returns a string representation of title
        return self.title


# Represents a comment on a blog post
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # One-to-many Relationship
