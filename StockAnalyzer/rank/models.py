from __future__ import unicode_literals
from yahoo_finance import Share
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):

    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    


