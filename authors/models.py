from django.db import models
import uuid

# Create your models here.

class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False, primary_key=True)
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='./images/', max_length=None,blank=True)