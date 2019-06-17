# Create your models here.

import os

from django.db import models
from urllib.parse import urlparse

from django.core.files import File
from django.core.exceptions import ValidationError

from django.conf import settings
# Create your models here.


def validate_file_extension(file):
    extension = os.path.splitext(file.name)[1]
    valid_extensions = [".pdf"]
    if not extension.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")


class Post(models.Model):
	profile_pic = models.ImageField(upload_to="")
	photo = models.ImageField(blank=True, upload_to="")
pdf = models.FileField(blank=True, upload_to="")


class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True, validators=[validate_file_extension])

    def __str__(self):
        return self.title
