from django.db import models
from news import settings
import uuid

# Create your models here.

class Base(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)
    title = models.CharField(max_length=60, null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

class Category(Base):
    pass

class Article(Base):
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
    )
    summary = models.CharField(max_length=256)
    firstParagraph = models.TextField()
    body = models.TextField()

    