# Create your models here.

from django.db import models
from urllib.parse import urlparse

from django.core.files import File

from django.conf import settings
# Create your models here.


class Post(models.Model):
	profile_pic = models.ImageField(upload_to="")
	photo = models.ImageField(blank=True, upload_to="")
pdf = models.FileField(blank=True, upload_to="")


class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)

    def __str__(self):
        return self.title
