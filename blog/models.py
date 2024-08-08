from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(50)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts")  # one-to-many Relationship
