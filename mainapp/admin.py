from django.contrib import admin
from .models import UploadFileModel
from .models import Post
# Register your models here.


admin.site.register(UploadFileModel)
admin.site.register(Post)