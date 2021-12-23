from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'is_active')
        
    def clean_title(self):
        data = self.cleaned_data['title']
        if len(data) < 3:
            raise ValidationError("At least three letters required")

        return data