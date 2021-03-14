from django.db import models
from authors.models import Author
import uuid

# Create your models here.

class Article(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    category = models.SlugField(max_length=64)
    title = models.CharField(max_length=60, null=False)
    summary = models.CharField(max_length=256)
    firstParagraph = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    