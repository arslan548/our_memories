from django import forms
from .models import MemoryImage
from .models import MemoryVideo

class MemoryImageForm(forms.ModelForm):
    class Meta:
        model = MemoryImage
        fields = ['title', 'image']


class MemoryVideoForm(forms.ModelForm):
    class Meta:
        model = MemoryVideo
        fields = ['title', 'video_file', 'youtube_link']

from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
