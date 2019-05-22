from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('Upload/', views.upload_file, name='upload'),
    path('Send/', views.upload_final, name='send'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

