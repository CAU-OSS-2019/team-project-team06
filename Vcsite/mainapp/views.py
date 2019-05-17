from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django import forms
from .forms import UploadFileForm
from .forms import UploadFileForm2
from .forms import UploadFileModel
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from mainapp.models import UploadFileModel
from mainapp.models import Post


def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))