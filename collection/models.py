from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, blank=True, null=True)
    startedOn = models.DateField(blank=True, null=True)
    finishedOn = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    author = models.TextField(default="Author Authorson")
