from django import forms

from uploads.models import Video


class UploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'name', 'sureName', 'email', 'video')
