from django import forms

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('url', )
        widgets = {
            'url': forms.TextInput(attrs={
                'placeholder': 'ex: https://www.youtube.com/watch?v=rA-RgGA_ZyY'
            })
        }
