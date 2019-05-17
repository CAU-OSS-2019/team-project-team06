'''from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()'''

from django import forms

from .models import UploadFileModel
from .models import Post

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False

class UploadFileForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('profile_pic', 'photo')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm2, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].required = False