from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.

def validate_image(fieldfile_obj):
    file_size = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if file_size > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
    else:
        return fieldfile_obj


class Forum(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='media/forum', height_field=None,
        width_field=None, max_length=100, null=False,
        blank=False, validators=[validate_image])

    def __str__(self):
        return self.title
