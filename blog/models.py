from django.db import models
from django.core.validators import MinLengthValidator


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(50)])
