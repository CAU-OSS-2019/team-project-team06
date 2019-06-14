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
from mainapp.pdf2jpg import convert
import asyncio
from Vcsite import settings
import glob, os, os.path

import threading

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            # Make instance of all files.
            for f in request.FILES.getlist('uploadfile'):
                instance = UploadFileModel(title= f.name, file=f)
                instance.save()
    else:
        '''form = UploadFileForm()'''
    return render(request, 'mainapp/index.html')

def convert_thread(path,dpi):
    convert(path,dpi)
    filelist = glob.glob(os.path.join(path,"*"))
    for f in filelist:
        os.remove(f)

@csrf_exempt
def upload_final(request):
    if request.method == 'POST':
        form = UploadFileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('/mainapp/'))
    else:
        '''form = UploadFileForm()'''
    thread = threading.Thread(target=convert_thread,
                                args=(
                                    'mainapp/input',
                                    200,
                                    ))
    thread.start()
    return render(request, 'mainapp/index.html')

def index(request):
    template = loader.get_template('mainapp/index.html')
    context = {
        'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))
