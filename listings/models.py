from django.db import models
from profiles.models import Profile

class Listing(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    price = models.SmallIntegerField()
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    likers = models.JSONField(default=dict)
    tags = models.JSONField(default=dict)