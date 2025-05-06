from django import forms
from .models import MemoryImage, MemoryVideo, Link, Note

class MemoryImageForm(forms.ModelForm):
    class Meta:
        model = MemoryImage
        fields = ['title', 'image']

class MemoryVideoForm(forms.ModelForm):
    class Meta:
        model = MemoryVideo
        fields = ['title', 'video_file', 'youtube_link']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
