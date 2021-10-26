from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Forum(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/forum', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.title

