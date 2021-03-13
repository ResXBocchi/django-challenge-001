from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4,editable=False)
    picture = models.ImageField(upload_to='./images/', max_length=None,blank=True)

    class Meta:
        ordering = ('id',)